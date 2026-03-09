from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.common import StatusResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=StatusResponse)
async def health_check(db: AsyncSession = Depends(get_db)) -> StatusResponse:
    try:
        await db.execute(text("SELECT 1"))
        return StatusResponse(status="healthy", message="All systems operational")
    except Exception as e:
        return StatusResponse(status="unhealthy", message=str(e))
