from __future__ import annotations

import json

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "STRATA"
    debug: bool = False

    # Database
    database_url: str = Field(alias="DATABASE_URL")

    # Security
    secret_key: str = Field(alias="SECRET_KEY")
    session_max_age: int = 86400  # 24 hours

    # LLM
    llm_provider: str = "mock"  # "openai" | "anthropic" | "mock"
    anthropic_api_key: str | None = None
    openai_api_key: str | None = None

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            return json.loads(v)
        return v

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


settings = Settings()  # type: ignore[call-arg]
