from __future__ import annotations

from collections.abc import Callable

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.config import settings
from app.database import get_db
from app.models.session import UserSession
from app.models.user import User
from app.services.core.llm_client import LLMClient


async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> User:
    session_token = request.cookies.get("session_id")
    if not session_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )

    from sqlalchemy import func

    result = await db.execute(
        select(UserSession)
        .options(selectinload(UserSession.user))
        .where(
            UserSession.token == session_token,
            UserSession.expires_at > func.now(),
        )
    )
    user_session = result.scalar_one_or_none()

    if not user_session or not user_session.user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session",
        )

    request.state.user_id = user_session.user.id
    return user_session.user


def require_role(*roles: str) -> Callable:
    async def checker(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user
    return checker


def get_llm_client() -> LLMClient:
    api_key = None
    if settings.llm_provider == "anthropic":
        api_key = settings.anthropic_api_key
    elif settings.llm_provider == "openai":
        api_key = settings.openai_api_key

    return LLMClient(
        provider=settings.llm_provider,
        api_key=api_key,
    )
