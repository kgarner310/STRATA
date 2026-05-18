from __future__ import annotations

import asyncio
import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///./strata_live_smoke.db")
os.environ.setdefault("SECRET_KEY", "local-smoke-secret")
os.environ.setdefault("LLM_PROVIDER", "anthropic")
os.environ.setdefault("DEBUG", "true")

from app.models import Base  # noqa: E402
from app.models.account import Account  # noqa: E402
from app.models.user import User  # noqa: E402
from app.services.analysis.service import AnalysisService  # noqa: E402
from app.services.coverage.service import CoverageService  # noqa: E402
from app.services.core.llm_client import LLMClient  # noqa: E402
from app.services.market.service import MarketService  # noqa: E402
from app.services.strategy.service import StrategyService  # noqa: E402
from app.utils.security import hash_password  # noqa: E402


def provider_key(provider: str) -> str | None:
    if provider == "anthropic":
        return os.environ.get("ANTHROPIC_API_KEY")
    if provider == "openai":
        return os.environ.get("OPENAI_API_KEY")
    return None


async def main() -> None:
    provider = os.environ.get("LLM_PROVIDER", "anthropic")
    api_key = provider_key(provider)

    if provider != "mock" and not api_key:
        raise SystemExit(f"{provider.upper()}_API_KEY is not set")

    engine = create_async_engine(os.environ["DATABASE_URL"])
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    async with session_factory() as db:
        user = User(
            email="live-smoke@strata.local",
            hashed_password=hash_password("test"),
            full_name="Live Smoke",
            role="producer",
        )
        db.add(user)
        await db.flush()

        account = Account(
            business_name="Piedmont Specialty Roofing",
            business_type="other",
            naics_code="238160",
            address="100 Trade Street",
            city="Charlotte",
            state="NC",
            zip_code="28202",
            annual_revenue=18_500_000,
            employee_count=84,
            vehicle_count=31,
            years_in_business=14,
            current_policies=[],
            description=(
                "Commercial roofing contractor doing low-slope membrane roofing, occupied-building repairs, "
                "emergency leak response, subcontracted specialty work, and school/healthcare projects."
            ),
            additional_notes=(
                "Need producer brief, submission plan, and submission narrative. "
                "Avoid static carrier appetite assumptions."
            ),
            created_by=user.id,
        )
        db.add(account)
        await db.flush()

        llm = LLMClient(provider=provider, api_key=api_key, model=os.environ.get("LLM_MODEL"))
        try:
            analysis = await AnalysisService(db, llm).analyze(account.id)
            coverage = await CoverageService(db, llm).analyze(account.id)
            strategy = await StrategyService(db, llm).analyze(account.id)
            market = await MarketService(db, llm).analyze(account.id)
        finally:
            await llm.close()

        print(
            {
                "provider": provider,
                "analysis_risk_score": analysis.get("risk_score"),
                "coverage_gaps": len(coverage.get("gaps", [])),
                "placement_paths": [
                    target.get("carrier_name") for target in strategy.get("target_carriers", [])
                ],
                "market_conversations": [
                    item.get("carrier_name") for item in market.get("carrier_intel", [])
                ],
            }
        )

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
