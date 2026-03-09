from __future__ import annotations

import json

import httpx

from app.utils.logging import get_logger

logger = get_logger(__name__)

DEFAULT_MODELS = {
    "openai": "gpt-4o",
    "anthropic": "claude-sonnet-4-20250514",
}


class LLMClient:
    def __init__(
        self,
        provider: str,
        api_key: str | None = None,
        model: str | None = None,
    ):
        self.provider = provider
        self.api_key = api_key
        self.model = model or DEFAULT_MODELS.get(provider, "")
        self._http = httpx.AsyncClient(timeout=60.0)

    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        if self.provider == "mock":
            return ""

        if self.provider == "openai":
            return await self._openai_complete(system_prompt, user_prompt)
        elif self.provider == "anthropic":
            return await self._anthropic_complete(system_prompt, user_prompt)

        raise ValueError(f"Unknown LLM provider: {self.provider}")

    async def complete_json(self, system_prompt: str, user_prompt: str) -> dict:
        raw = await self.complete(system_prompt, user_prompt)
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown code blocks
            if "```json" in raw:
                start = raw.index("```json") + 7
                end = raw.index("```", start)
                return json.loads(raw[start:end].strip())
            if "```" in raw:
                start = raw.index("```") + 3
                end = raw.index("```", start)
                return json.loads(raw[start:end].strip())
            logger.error("Failed to parse LLM JSON response", raw_response=raw[:200])
            raise

    async def _openai_complete(self, system: str, user: str) -> str:
        resp = await self._http.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.3,
                "response_format": {"type": "json_object"},
            },
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    async def _anthropic_complete(self, system: str, user: str) -> str:
        resp = await self._http.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self.api_key or "",
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": self.model,
                "max_tokens": 4096,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            },
        )
        resp.raise_for_status()
        return resp.json()["content"][0]["text"]

    async def close(self) -> None:
        await self._http.aclose()
