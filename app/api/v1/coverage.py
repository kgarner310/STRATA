from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.audit.service import AuditService
from app.database import get_db
from app.dependencies import get_current_user, get_llm_client
from app.models.user import User
from app.schemas.coverage import CoverageResponse
from app.services.core.llm_client import LLMClient
from app.services.coverage.service import CoverageService

router = APIRouter(prefix="/coverage", tags=["coverage"])


@router.get("/gaps/{account_id}", response_model=CoverageResponse)
async def get_coverage_gaps(
    account_id: uuid.UUID,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
    llm: LLMClient = Depends(get_llm_client),
) -> dict:
    service = CoverageService(db=db, llm_client=llm)
    result = await service.get_or_analyze(account_id)

    audit = AuditService(db)
    await audit.log_action(
        "coverage_reasoning_generated",
        user_id=user.id,
        resource_type="account",
        resource_id=str(account_id),
        ip_address=request.client.host if request.client else None,
    )

    return {**result, "account_id": account_id}
