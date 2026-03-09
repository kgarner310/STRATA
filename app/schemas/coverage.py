from __future__ import annotations

import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class CoverageGapItem(BaseModel):
    line_of_business: str
    gap_type: Literal["missing", "inadequate_limit", "exclusion_risk", "sublimit_concern"]
    severity: Literal["low", "medium", "high", "critical"]
    description: str
    recommendation: str
    potential_impact: str | None = None


class CoverageRecommendation(BaseModel):
    line_of_business: str
    recommendation: str
    rationale: str
    priority: Literal["low", "medium", "high"]


class CoverageResponse(BaseModel):
    account_id: uuid.UUID
    gaps: list[CoverageGapItem]
    recommendations: list[CoverageRecommendation]
    adequacy_score: int
    summary: str
    computed_at: datetime
