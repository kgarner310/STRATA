from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.audit.service import AuditService
from app.database import get_db
from app.dependencies import get_current_user, get_llm_client
from app.models.user import User
from app.schemas.analysis import AnalysisResponse
from app.services.analysis.service import AnalysisService
from app.services.core.llm_client import LLMClient

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.get("/{account_id}", response_model=AnalysisResponse)
async def get_analysis(
    account_id: uuid.UUID,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
    llm: LLMClient = Depends(get_llm_client),
) -> dict:
    service = AnalysisService(db=db, llm_client=llm)
    result = await service.get_or_analyze(account_id)

    audit = AuditService(db)
    await audit.log_action(
        "analysis_run",
        user_id=user.id,
        resource_type="account",
        resource_id=str(account_id),
        ip_address=request.client.host if request.client else None,
    )

    return {**result, "account_id": account_id}
