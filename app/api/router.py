from __future__ import annotations

from fastapi import APIRouter

from app.api.v1 import accounts, analysis, auth, brief, coverage, health, market, strategy

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(accounts.router)
api_router.include_router(analysis.router)
api_router.include_router(coverage.router)
api_router.include_router(strategy.router)
api_router.include_router(market.router)
api_router.include_router(brief.router)
