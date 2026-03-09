from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel


class BriefSection(BaseModel):
    label: str
    content: str


class ParkingLotBriefResponse(BaseModel):
    account_id: uuid.UUID
    account_name: str
    industry: str
    employee_count: int | None
    annual_revenue: float | None
    vehicle_count: int | None
    things_to_confirm: list[str]
    coverage_to_discuss: str
    underwriter_concern: str
    opening_talking_point: str
    risk_score: int | None = None
    computed_at: datetime
