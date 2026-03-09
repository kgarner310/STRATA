from __future__ import annotations

import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class SubmissionTarget(BaseModel):
    carrier_name: str
    appetite_level: Literal["strong", "moderate", "limited"]
    rationale: str
    key_concerns: list[str] = []


class PositioningNote(BaseModel):
    topic: str
    framing: str
    supporting_evidence: str | None = None


class StrategyResponse(BaseModel):
    account_id: uuid.UUID
    target_carriers: list[SubmissionTarget]
    positioning_notes: list[PositioningNote]
    submission_summary: str
    key_differentiators: list[str]
    underwriter_concerns: list[str]
    computed_at: datetime
