from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class ExposureItem(BaseModel):
    type: str
    severity: Literal["low", "medium", "high", "critical"]
    description: str
    mitigation_notes: str | None = None


class TalkingPoint(BaseModel):
    topic: str
    point: str
    supporting_data: str | None = None


class AnalysisResponse(BaseModel):
    account_id: uuid.UUID
    risk_score: int = Field(ge=0, le=100)
    key_exposures: list[ExposureItem]
    industry_benchmarks: dict[str, Any] = {}
    talking_points: list[TalkingPoint]
    questions_to_ask: list[str]
    computed_at: datetime
