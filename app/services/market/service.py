from __future__ import annotations

import uuid

from app.services.core.base import BasePillarService
from app.services.core.mock_responses import MOCK_MARKET

SYSTEM_PROMPT = """You are a commercial insurance market intelligence analyst. Provide current market signals,
carrier intelligence, and industry outlook for the given account. Return as JSON with:
{
    "signals": [{"signal_type": "trend"|"alert"|"opportunity"|"risk", "title": str, "description": str,
                 "relevance": "low"|"medium"|"high", "source": str}],
    "carrier_intel": [{"carrier_name": str, "market_position": str, "appetite_notes": str, "recent_changes": str}],
    "industry_outlook": str,
    "talking_points": [str]
}"""


class MarketService(BasePillarService):
    RESULT_TYPE = "market_intelligence"

    async def analyze(self, account_id: uuid.UUID) -> dict:
        account = await self._get_account(account_id)

        if self.llm_client.provider == "mock":
            mock_data = MOCK_MARKET.get(account.business_type, MOCK_MARKET["restaurant"])
            return {**mock_data, "account_id": str(account_id)}

        prompt = self.prompt_engine.render(
            "market/carrier_intel.jinja2",
            business_name=account.business_name,
            business_type=account.business_type,
            revenue=account.annual_revenue,
            employee_count=account.employee_count,
            state=account.state,
            city=account.city,
            current_policies=account.current_policies,
        )

        result = await self.llm_client.complete_json(SYSTEM_PROMPT, prompt)
        result["account_id"] = str(account_id)
        return result
