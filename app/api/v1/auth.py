from __future__ import annotations

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.audit.service import AuditService
from app.config import settings
from app.database import get_db
from app.dependencies import get_current_user, require_role
from app.models.session import UserSession
from app.models.user import User
from app.schemas.auth import LoginRequest, UserCreate, UserResponse
from app.utils.security import generate_session_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserResponse)
async def login(
    body: LoginRequest,
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
) -> User:
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()

    audit = AuditService(db)

    if not user or not verify_password(body.password, user.hashed_password):
        await audit.log_action(
            "failed_login",
            ip_address=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent"),
            metadata={"email": body.email},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled",
        )

    now = datetime.now(timezone.utc)
    session = UserSession(
        user_id=user.id,
        token=generate_session_token(),
        created_at=now,
        expires_at=now + timedelta(seconds=settings.session_max_age),
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
    )
    db.add(session)
    await db.flush()

    await audit.log_action(
        "login",
        user_id=user.id,
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
    )

    response.set_cookie(
        key="session_id",
        value=session.token,
        httponly=True,
        secure=not settings.debug,
        samesite="lax",
        max_age=settings.session_max_age,
    )

    return user


@router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> dict[str, str]:
    session_token = request.cookies.get("session_id")
    if session_token:
        result = await db.execute(
            select(UserSession).where(UserSession.token == session_token)
        )
        session = result.scalar_one_or_none()
        if session:
            await db.delete(session)

    audit = AuditService(db)
    await audit.log_action(
        "logout",
        user_id=user.id,
        ip_address=request.client.host if request.client else None,
    )

    response.delete_cookie("session_id")
    return {"message": "Logged out"}


@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(get_current_user)) -> User:
    return user


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    body: UserCreate,
    request: Request,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_role("admin")),
) -> User:
    existing = await db.execute(select(User).where(User.email == body.email))
    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    user = User(
        email=body.email,
        hashed_password=hash_password(body.password),
        full_name=body.full_name,
        role=body.role,
    )
    db.add(user)
    await db.flush()

    audit = AuditService(db)
    await audit.log_action(
        "account_created",
        user_id=admin.id,
        resource_type="user",
        resource_id=str(user.id),
        ip_address=request.client.host if request.client else None,
    )

    return user
