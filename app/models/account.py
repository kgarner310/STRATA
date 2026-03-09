from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy import JSON, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin


class Account(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "accounts"

    business_name: Mapped[str] = mapped_column(String(200), nullable=False)
    business_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    naics_code: Mapped[str | None] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(2), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)
    annual_revenue: Mapped[float | None] = mapped_column()
    employee_count: Mapped[int | None] = mapped_column()
    vehicle_count: Mapped[int | None] = mapped_column()
    years_in_business: Mapped[int | None] = mapped_column()
    current_policies: Mapped[dict[str, Any]] = mapped_column(JSON, default=list)
    description: Mapped[str | None] = mapped_column(Text)
    additional_notes: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="active")

    created_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    created_by_user: Mapped[User] = relationship(back_populates="accounts")  # noqa: F821

    analysis_results: Mapped[list[AnalysisResult]] = relationship(  # noqa: F821
        back_populates="account", cascade="all, delete-orphan"
    )
