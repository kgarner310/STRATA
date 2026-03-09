from __future__ import annotations

import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.audit.service import AuditService
from app.database import async_session_factory


class AuditLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        response = await call_next(request)

        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            try:
                async with async_session_factory() as db:
                    audit = AuditService(db)
                    await audit.log_action(
                        action=f"{request.method} {request.url.path}",
                        user_id=getattr(request.state, "user_id", None),
                        ip_address=request.client.host if request.client else None,
                        user_agent=request.headers.get("user-agent"),
                        request_id=request_id,
                        metadata={"status_code": response.status_code},
                    )
                    await db.commit()
            except Exception:
                pass  # Audit logging should never break the request

        return response
