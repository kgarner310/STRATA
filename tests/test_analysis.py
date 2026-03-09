from __future__ import annotations

import pytest
from httpx import AsyncClient


SAMPLE_ACCOUNT = {
    "business_name": "Test Restaurant",
    "business_type": "restaurant",
    "address": "123 Main Street",
    "city": "Philadelphia",
    "state": "PA",
    "zip_code": "19103",
    "annual_revenue": 1500000,
    "employee_count": 20,
}


@pytest.mark.asyncio
async def test_get_analysis(authenticated_client: AsyncClient):
    # Create account first
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake", json=SAMPLE_ACCOUNT
    )
    account_id = create_resp.json()["id"]

    # Get analysis (mock provider returns pre-computed data)
    response = await authenticated_client.get(f"/api/v1/analysis/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert "risk_score" in data
    assert "key_exposures" in data
    assert "talking_points" in data
    assert "questions_to_ask" in data
    assert data["risk_score"] >= 0
    assert data["risk_score"] <= 100


@pytest.mark.asyncio
async def test_get_coverage_gaps(authenticated_client: AsyncClient):
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake", json=SAMPLE_ACCOUNT
    )
    account_id = create_resp.json()["id"]

    response = await authenticated_client.get(f"/api/v1/coverage/gaps/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert "gaps" in data
    assert "recommendations" in data
    assert "adequacy_score" in data


@pytest.mark.asyncio
async def test_get_strategy(authenticated_client: AsyncClient):
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake", json=SAMPLE_ACCOUNT
    )
    account_id = create_resp.json()["id"]

    response = await authenticated_client.get(f"/api/v1/strategy/submission/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert "target_carriers" in data
    assert "positioning_notes" in data
    assert "submission_summary" in data


@pytest.mark.asyncio
async def test_get_market_intel(authenticated_client: AsyncClient):
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake", json=SAMPLE_ACCOUNT
    )
    account_id = create_resp.json()["id"]

    response = await authenticated_client.get(f"/api/v1/market/intel/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert "signals" in data
    assert "carrier_intel" in data
    assert "industry_outlook" in data


@pytest.mark.asyncio
async def test_analysis_unauthenticated(client: AsyncClient):
    response = await client.get(
        "/api/v1/analysis/00000000-0000-0000-0000-000000000000"
    )
    assert response.status_code == 401
