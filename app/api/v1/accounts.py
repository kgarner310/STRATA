from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.audit.service import AuditService
from app.database import get_db
from app.dependencies import get_current_user
from app.models.account import Account
from app.models.user import User
from app.schemas.account import AccountIntakeRequest, AccountResponse, AccountSummary

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/intake", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def intake_account(
    body: AccountIntakeRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> Account:
    account = Account(
        business_name=body.business_name,
        business_type=body.business_type.value,
        naics_code=body.naics_code,
        address=body.address,
        city=body.city,
        state=body.state,
        zip_code=body.zip_code,
        annual_revenue=body.annual_revenue,
        employee_count=body.employee_count,
        vehicle_count=body.vehicle_count,
        years_in_business=body.years_in_business,
        current_policies=[p.model_dump(mode="json") for p in body.current_policies],
        description=body.description,
        additional_notes=body.additional_notes,
        created_by=user.id,
    )
    db.add(account)
    await db.flush()

    audit = AuditService(db)
    await audit.log_action(
        "account_created",
        user_id=user.id,
        resource_type="account",
        resource_id=str(account.id),
        ip_address=request.client.host if request.client else None,
    )

    return account


@router.get("", response_model=list[AccountSummary])
async def list_accounts(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> list[Account]:
    result = await db.execute(
        select(Account).order_by(Account.created_at.desc())
    )
    return list(result.scalars().all())


@router.get("/{account_id}", response_model=AccountResponse)
async def get_account(
    account_id: uuid.UUID,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> Account:
    result = await db.execute(select(Account).where(Account.id == account_id))
    account = result.scalar_one_or_none()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account '{account_id}' not found",
        )

    audit = AuditService(db)
    await audit.log_action(
        "account_viewed",
        user_id=user.id,
        resource_type="account",
        resource_id=str(account.id),
        ip_address=request.client.host if request.client else None,
    )

    return account
