from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import JSON, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, UUIDMixin


class AnalysisResult(UUIDMixin, Base):
    __tablename__ = "analysis_results"

    account_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False, index=True
    )
    result_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    computed_at: Mapped[datetime] = mapped_column(server_default=func.now())
    is_stale: Mapped[bool] = mapped_column(default=False)

    account: Mapped[Account] = relationship(back_populates="analysis_results")  # noqa: F821
