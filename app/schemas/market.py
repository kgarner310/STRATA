from __future__ import annotations

import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class MarketSignal(BaseModel):
    signal_type: Literal["trend", "alert", "opportunity", "risk"]
    title: str
    description: str
    relevance: Literal["low", "medium", "high"]
    source: str | None = None


class CarrierIntel(BaseModel):
    carrier_name: str
    market_position: str
    appetite_notes: str
    recent_changes: str | None = None


class MarketResponse(BaseModel):
    account_id: uuid.UUID
    signals: list[MarketSignal]
    carrier_intel: list[CarrierIntel]
    industry_outlook: str
    talking_points: list[str]
    computed_at: datetime
