from __future__ import annotations

import uuid
from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class BusinessType(str, Enum):
    RESTAURANT = "restaurant"
    LANDSCAPING = "landscaping"
    MANUFACTURING = "manufacturing"
    APARTMENT_COMPLEX = "apartment_complex"
    OTHER = "other"


class PolicyInfo(BaseModel):
    carrier: str
    line_of_business: str
    premium: float | None = None
    effective_date: date | None = None
    expiration_date: date | None = None
    limits: dict[str, Any] = {}
    deductibles: dict[str, Any] = {}


class AccountIntakeRequest(BaseModel):
    business_name: str = Field(..., min_length=1, max_length=200)
    business_type: BusinessType
    naics_code: str | None = None
    address: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    state: str = Field(..., pattern=r"^[A-Z]{2}$")
    zip_code: str = Field(..., pattern=r"^\d{5}(-\d{4})?$")
    annual_revenue: float | None = None
    employee_count: int | None = Field(default=None, ge=0)
    vehicle_count: int | None = Field(default=None, ge=0)
    years_in_business: int | None = Field(default=None, ge=0)
    current_policies: list[PolicyInfo] = []
    description: str | None = None
    additional_notes: str | None = None


class AccountResponse(BaseModel):
    id: uuid.UUID
    business_name: str
    business_type: str
    naics_code: str | None
    address: str
    city: str
    state: str
    zip_code: str
    annual_revenue: float | None
    employee_count: int | None
    vehicle_count: int | None
    years_in_business: int | None
    current_policies: list[dict[str, Any]]
    description: str | None
    additional_notes: str | None
    status: str
    created_by: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class AccountSummary(BaseModel):
    id: uuid.UUID
    business_name: str
    business_type: str
    city: str
    state: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
