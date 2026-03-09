from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.audit.service import AuditService
from app.database import get_db
from app.dependencies import get_current_user, get_llm_client
from app.models.user import User
from app.schemas.brief import ParkingLotBriefResponse
from app.services.brief.service import BriefService
from app.services.core.llm_client import LLMClient

router = APIRouter(prefix="/brief", tags=["brief"])


@router.get("/parking-lot/{account_id}", response_model=ParkingLotBriefResponse)
async def get_parking_lot_brief(
    account_id: uuid.UUID,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
    llm: LLMClient = Depends(get_llm_client),
) -> dict:
    service = BriefService(db=db, llm_client=llm)
    result = await service.generate_brief(account_id)

    audit = AuditService(db)
    await audit.log_action(
        "parking_lot_brief_generated",
        user_id=user.id,
        resource_type="account",
        resource_id=str(account_id),
        ip_address=request.client.host if request.client else None,
    )

    return result
