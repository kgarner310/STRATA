from __future__ import annotations

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    detail: str


class StatusResponse(BaseModel):
    status: str
    message: str | None = None
