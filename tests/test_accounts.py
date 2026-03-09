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
    "current_policies": [],
}


@pytest.mark.asyncio
async def test_create_account(authenticated_client: AsyncClient):
    response = await authenticated_client.post(
        "/api/v1/accounts/intake",
        json=SAMPLE_ACCOUNT,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["business_name"] == "Test Restaurant"
    assert data["business_type"] == "restaurant"
    assert data["state"] == "PA"
    assert "id" in data


@pytest.mark.asyncio
async def test_create_account_unauthenticated(client: AsyncClient):
    response = await client.post(
        "/api/v1/accounts/intake",
        json=SAMPLE_ACCOUNT,
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_account(authenticated_client: AsyncClient):
    # Create first
    create_resp = await authenticated_client.post(
        "/api/v1/accounts/intake",
        json=SAMPLE_ACCOUNT,
    )
    account_id = create_resp.json()["id"]

    # Then fetch
    response = await authenticated_client.get(f"/api/v1/accounts/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == account_id
    assert data["business_name"] == "Test Restaurant"


@pytest.mark.asyncio
async def test_get_nonexistent_account(authenticated_client: AsyncClient):
    response = await authenticated_client.get(
        "/api/v1/accounts/00000000-0000-0000-0000-000000000000"
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_accounts(authenticated_client: AsyncClient):
    # Create two accounts
    await authenticated_client.post("/api/v1/accounts/intake", json=SAMPLE_ACCOUNT)
    await authenticated_client.post(
        "/api/v1/accounts/intake",
        json={**SAMPLE_ACCOUNT, "business_name": "Second Restaurant"},
    )

    response = await authenticated_client.get("/api/v1/accounts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2


@pytest.mark.asyncio
async def test_create_account_validation(authenticated_client: AsyncClient):
    # Invalid state code
    response = await authenticated_client.post(
        "/api/v1/accounts/intake",
        json={**SAMPLE_ACCOUNT, "state": "Pennsylvania"},
    )
    assert response.status_code == 422

    # Invalid zip code
    response = await authenticated_client.post(
        "/api/v1/accounts/intake",
        json={**SAMPLE_ACCOUNT, "zip_code": "abc"},
    )
    assert response.status_code == 422
