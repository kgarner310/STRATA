from __future__ import annotations

import uuid

from app.services.core.base import BasePillarService
from app.services.core.mock_responses import MOCK_ANALYSIS

SYSTEM_PROMPT = """You are an expert commercial insurance risk analyst. Analyze the provided business account
and identify key exposures, risk factors, and industry-specific concerns. Return your analysis as JSON with
the following structure:
{
    "risk_score": <int 0-100>,
    "key_exposures": [{"type": str, "severity": "low"|"medium"|"high"|"critical", "description": str, "mitigation_notes": str}],
    "industry_benchmarks": {<relevant metrics>},
    "talking_points": [{"topic": str, "point": str, "supporting_data": str}],
    "questions_to_ask": [<list of discovery questions>]
}"""


class AnalysisService(BasePillarService):
    RESULT_TYPE = "account_analysis"

    async def analyze(self, account_id: uuid.UUID) -> dict:
        account = await self._get_account(account_id)

        if self.llm_client.provider == "mock":
            mock_data = MOCK_ANALYSIS.get(account.business_type, MOCK_ANALYSIS["restaurant"])
            return {**mock_data, "account_id": str(account_id)}

        prompt = self.prompt_engine.render(
            "analysis/exposure_analysis.jinja2",
            business_name=account.business_name,
            business_type=account.business_type,
            naics_code=account.naics_code,
            revenue=account.annual_revenue,
            employee_count=account.employee_count,
            vehicle_count=account.vehicle_count,
            years_in_business=account.years_in_business,
            current_policies=account.current_policies,
            state=account.state,
            city=account.city,
            description=account.description,
        )

        result = await self.llm_client.complete_json(SYSTEM_PROMPT, prompt)
        result["account_id"] = str(account_id)
        return result
