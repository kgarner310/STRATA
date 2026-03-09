from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.audit.middleware import AuditLogMiddleware
from app.config import settings
from app.database import engine
from app.utils.exceptions import StrataException, strata_exception_handler
from app.utils.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    setup_logging()
    # Verify DB connection on startup
    async with engine.begin() as conn:
        pass
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title="STRATA",
        description="AI reasoning engine for commercial insurance producers",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(AuditLogMiddleware)

    app.add_exception_handler(StrataException, strata_exception_handler)

    app.include_router(api_router)

    return app


app = create_app()
