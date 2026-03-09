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
async def test_parking_lot_brief(authenticated_client: AsyncClient):
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake", json=SAMPLE_ACCOUNT
    )
    account_id = create_resp.json()["id"]

    response = await authenticated_client.get(f"/api/v1/brief/parking-lot/{account_id}")
    assert response.status_code == 200
    data = response.json()

    # Verify the parking lot brief format
    assert data["account_name"] == "Test Restaurant"
    assert "industry" in data
    assert "things_to_confirm" in data
    assert len(data["things_to_confirm"]) == 3
    assert "coverage_to_discuss" in data
    assert "underwriter_concern" in data
    assert "opening_talking_point" in data
    assert data["employee_count"] == 20
    assert data["annual_revenue"] == 1500000


@pytest.mark.asyncio
async def test_brief_nonexistent_account(authenticated_client: AsyncClient):
    response = await authenticated_client.get(
        "/api/v1/brief/parking-lot/00000000-0000-0000-0000-000000000000"
    )
    assert response.status_code == 404
