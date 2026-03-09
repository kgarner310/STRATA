"""Seed script for demo data.

Usage: python -m app.seeds.seed_all
"""
from __future__ import annotations

import asyncio
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


async def seed() -> None:
    from app.database import async_session_factory, engine
    from app.models import Base
    from app.models.account import Account
    from app.models.analysis import AnalysisResult
    from app.models.user import User
    from app.seeds.demo_accounts import DEMO_ACCOUNTS
    from app.services.core.mock_responses import (
        MOCK_ANALYSIS,
        MOCK_BRIEFS,
        MOCK_COVERAGE,
        MOCK_MARKET,
        MOCK_STRATEGY,
    )
    from app.utils.security import hash_password

    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_factory() as db:
        # Check if data already exists
        from sqlalchemy import select, func

        user_count = await db.scalar(select(func.count()).select_from(User))
        if user_count and user_count > 0:
            print("Database already seeded. Skipping.")
            return

        # Create users
        admin = User(
            email="admin@keystone.com",
            hashed_password=hash_password("admin123!"),
            full_name="Admin User",
            role="admin",
        )
        producer = User(
            email="producer@keystone.com",
            hashed_password=hash_password("producer123!"),
            full_name="Sarah Mitchell",
            role="producer",
        )
        db.add_all([admin, producer])
        await db.flush()

        print(f"Created admin user: admin@keystone.com (password: admin123!)")
        print(f"Created producer user: producer@keystone.com (password: producer123!)")

        # Create demo accounts
        accounts = []
        for account_data in DEMO_ACCOUNTS:
            account = Account(
                **account_data,
                created_by=producer.id,
            )
            db.add(account)
            accounts.append(account)

        await db.flush()

        # Pre-compute analysis results for each account
        result_types = {
            "account_analysis": MOCK_ANALYSIS,
            "coverage_reasoning": MOCK_COVERAGE,
            "submission_strategy": MOCK_STRATEGY,
            "market_intelligence": MOCK_MARKET,
        }

        now = datetime.now(timezone.utc)
        for account in accounts:
            print(f"Seeding analysis for: {account.business_name}")
            for result_type, mock_data in result_types.items():
                data = mock_data.get(account.business_type, {})
                if data:
                    result = AnalysisResult(
                        account_id=account.id,
                        result_type=result_type,
                        data={**data, "account_id": str(account.id)},
                        computed_at=now,
                    )
                    db.add(result)

        await db.commit()
        print(f"\nSeeded {len(accounts)} demo accounts with pre-computed analysis results.")
        print("\nDemo accounts:")
        for account in accounts:
            print(f"  - {account.business_name} ({account.city}, {account.state})")


def main() -> None:
    print("STRATA Demo Data Seeder")
    print("=" * 40)
    asyncio.run(seed())
    print("\nDone!")


if __name__ == "__main__":
    main()
