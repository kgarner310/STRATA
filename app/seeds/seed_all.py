"""Seed script for initial users.

Usage: python -m app.seeds.seed_all
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


async def seed() -> None:
    from app.database import async_session_factory, engine
    from app.models import Base
    from app.models.user import User
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

        admin = User(
            email="admin@strata.local",
            hashed_password=hash_password("change-me-admin"),
            full_name="STRATA Admin",
            role="admin",
        )
        producer = User(
            email="producer@strata.local",
            hashed_password=hash_password("change-me-producer"),
            full_name="STRATA Producer",
            role="producer",
        )
        db.add_all([admin, producer])
        await db.commit()
        print("Created initial admin user: admin@strata.local")
        print("Created initial producer user: producer@strata.local")
        print("No demo accounts or pre-computed analyses were seeded.")


def main() -> None:
    print("STRATA Initial User Seeder")
    print("=" * 40)
    asyncio.run(seed())
    print("\nDone!")


if __name__ == "__main__":
    main()
