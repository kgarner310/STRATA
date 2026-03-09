from __future__ import annotations

import uuid

from app.services.core.base import BasePillarService
from app.services.core.mock_responses import MOCK_COVERAGE

SYSTEM_PROMPT = """You are an expert commercial insurance coverage analyst. Review the provided account's
current coverage and identify gaps, inadequacies, and recommendations. Return your analysis as JSON with:
{
    "gaps": [{"line_of_business": str, "gap_type": "missing"|"inadequate_limit"|"exclusion_risk"|"sublimit_concern",
              "severity": "low"|"medium"|"high"|"critical", "description": str, "recommendation": str, "potential_impact": str}],
    "recommendations": [{"line_of_business": str, "recommendation": str, "rationale": str, "priority": "low"|"medium"|"high"}],
    "adequacy_score": <int 0-100>,
    "summary": str
}"""


class CoverageService(BasePillarService):
    RESULT_TYPE = "coverage_reasoning"

    async def analyze(self, account_id: uuid.UUID) -> dict:
        account = await self._get_account(account_id)

        if self.llm_client.provider == "mock":
            mock_data = MOCK_COVERAGE.get(account.business_type, MOCK_COVERAGE["restaurant"])
            return {**mock_data, "account_id": str(account_id)}

        prompt = self.prompt_engine.render(
            "coverage/gap_detection.jinja2",
            business_name=account.business_name,
            business_type=account.business_type,
            revenue=account.annual_revenue,
            employee_count=account.employee_count,
            current_policies=account.current_policies,
            state=account.state,
            description=account.description,
        )

        result = await self.llm_client.complete_json(SYSTEM_PROMPT, prompt)
        result["account_id"] = str(account_id)
        return result
