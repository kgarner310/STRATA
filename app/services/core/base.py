from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analysis import AnalysisResult
from app.services.core.llm_client import LLMClient
from app.services.core.prompt_engine import prompt_engine


class BasePillarService(ABC):
    STALE_AFTER = timedelta(hours=24)
    RESULT_TYPE: str  # Override in subclasses

    def __init__(self, db: AsyncSession, llm_client: LLMClient):
        self.db = db
        self.llm_client = llm_client
        self.prompt_engine = prompt_engine

    @abstractmethod
    async def analyze(self, account_id: uuid.UUID) -> dict:
        ...

    async def get_cached_result(self, account_id: uuid.UUID) -> AnalysisResult | None:
        result = await self.db.execute(
            select(AnalysisResult)
            .where(
                AnalysisResult.account_id == account_id,
                AnalysisResult.result_type == self.RESULT_TYPE,
                AnalysisResult.is_stale == False,  # noqa: E712
            )
            .order_by(AnalysisResult.computed_at.desc())
        )
        return result.scalar_one_or_none()

    def _is_stale(self, result: AnalysisResult) -> bool:
        now = datetime.now(timezone.utc)
        computed = result.computed_at.replace(tzinfo=timezone.utc) if result.computed_at.tzinfo is None else result.computed_at
        return now - computed > self.STALE_AFTER

    async def get_or_analyze(self, account_id: uuid.UUID) -> dict:
        cached = await self.get_cached_result(account_id)
        if cached and not self._is_stale(cached):
            return cached.data

        fresh = await self.analyze(account_id)
        await self._store_result(account_id, fresh)
        return fresh

    async def _store_result(self, account_id: uuid.UUID, data: dict) -> None:
        # Mark old results as stale
        old_results = await self.db.execute(
            select(AnalysisResult).where(
                AnalysisResult.account_id == account_id,
                AnalysisResult.result_type == self.RESULT_TYPE,
            )
        )
        for old in old_results.scalars():
            old.is_stale = True

        result = AnalysisResult(
            account_id=account_id,
            result_type=self.RESULT_TYPE,
            data=data,
        )
        self.db.add(result)
        await self.db.flush()

    async def _get_account(self, account_id: uuid.UUID):
        from app.models.account import Account
        result = await self.db.execute(
            select(Account).where(Account.id == account_id)
        )
        account = result.scalar_one_or_none()
        if not account:
            from app.utils.exceptions import NotFoundError
            raise NotFoundError("Account", str(account_id))
        return account
