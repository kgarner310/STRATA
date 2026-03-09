from __future__ import annotations

import uuid

from app.services.core.base import BasePillarService
from app.services.core.mock_responses import MOCK_STRATEGY

SYSTEM_PROMPT = """You are an expert commercial insurance submission strategist. Analyze the account and
recommend target carriers, positioning strategy, and key differentiators. Return as JSON with:
{
    "target_carriers": [{"carrier_name": str, "appetite_level": "strong"|"moderate"|"limited",
                         "rationale": str, "key_concerns": [str]}],
    "positioning_notes": [{"topic": str, "framing": str, "supporting_evidence": str}],
    "submission_summary": str,
    "key_differentiators": [str],
    "underwriter_concerns": [str]
}"""


class StrategyService(BasePillarService):
    RESULT_TYPE = "submission_strategy"

    async def analyze(self, account_id: uuid.UUID) -> dict:
        account = await self._get_account(account_id)

        if self.llm_client.provider == "mock":
            mock_data = MOCK_STRATEGY.get(account.business_type, MOCK_STRATEGY["restaurant"])
            return {**mock_data, "account_id": str(account_id)}

        prompt = self.prompt_engine.render(
            "strategy/submission_plan.jinja2",
            business_name=account.business_name,
            business_type=account.business_type,
            revenue=account.annual_revenue,
            employee_count=account.employee_count,
            current_policies=account.current_policies,
            state=account.state,
            city=account.city,
            description=account.description,
        )

        result = await self.llm_client.complete_json(SYSTEM_PROMPT, prompt)
        result["account_id"] = str(account_id)
        return result
