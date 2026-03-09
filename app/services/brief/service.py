from __future__ import annotations

import asyncio
import uuid
from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.analysis.service import AnalysisService
from app.services.core.llm_client import LLMClient
from app.services.core.mock_responses import MOCK_BRIEFS
from app.services.coverage.service import CoverageService
from app.services.market.service import MarketService
from app.services.strategy.service import StrategyService


class BriefService:
    """Orchestrates all 4 pillars into a 10-second parking lot brief."""

    def __init__(self, db: AsyncSession, llm_client: LLMClient):
        self.db = db
        self.llm_client = llm_client
        self.analysis = AnalysisService(db, llm_client)
        self.coverage = CoverageService(db, llm_client)
        self.strategy = StrategyService(db, llm_client)
        self.market = MarketService(db, llm_client)

    async def generate_brief(self, account_id: uuid.UUID) -> dict:
        from app.models.account import Account
        from sqlalchemy import select

        result = await self.db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalar_one_or_none()
        if not account:
            from app.utils.exceptions import NotFoundError
            raise NotFoundError("Account", str(account_id))

        if self.llm_client.provider == "mock":
            brief_data = MOCK_BRIEFS.get(account.business_type, MOCK_BRIEFS["restaurant"])
            return {
                "account_id": str(account_id),
                "account_name": account.business_name,
                "employee_count": account.employee_count,
                "annual_revenue": account.annual_revenue,
                "vehicle_count": account.vehicle_count,
                **brief_data,
            }

        # Run all 4 pillar analyses concurrently
        analysis_data, coverage_data, strategy_data, market_data = await asyncio.gather(
            self.analysis.get_or_analyze(account_id),
            self.coverage.get_or_analyze(account_id),
            self.strategy.get_or_analyze(account_id),
            self.market.get_or_analyze(account_id),
        )

        return self._synthesize_brief(
            account=account,
            account_id=account_id,
            analysis=analysis_data,
            coverage=coverage_data,
            strategy=strategy_data,
            market=market_data,
        )

    def _synthesize_brief(
        self,
        account,
        account_id: uuid.UUID,
        analysis: dict,
        coverage: dict,
        strategy: dict,
        market: dict,
    ) -> dict:
        # Extract top 3 discovery questions from analysis
        questions = analysis.get("questions_to_ask", [])[:3]

        # Get the most critical coverage gap
        gaps = coverage.get("gaps", [])
        critical_gap = next(
            (g for g in gaps if g.get("severity") in ("critical", "high")),
            gaps[0] if gaps else {"description": "No critical gaps identified"},
        )

        # Get the top underwriter concern
        concerns = strategy.get("underwriter_concerns", [])
        top_concern = concerns[0] if concerns else "No specific concerns identified"

        # Get the best opening talking point from market
        market_points = market.get("talking_points", [])
        opening_point = market_points[0] if market_points else "Market conditions are favorable for this account."

        return {
            "account_id": str(account_id),
            "account_name": account.business_name,
            "industry": account.business_type.replace("_", " ").title(),
            "employee_count": account.employee_count,
            "annual_revenue": account.annual_revenue,
            "vehicle_count": account.vehicle_count,
            "things_to_confirm": questions,
            "coverage_to_discuss": critical_gap.get("description", str(critical_gap)),
            "underwriter_concern": top_concern,
            "opening_talking_point": opening_point,
            "risk_score": analysis.get("risk_score"),
            "computed_at": datetime.now(timezone.utc).isoformat(),
        }
