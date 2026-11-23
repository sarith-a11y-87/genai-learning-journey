"""Settings loaded from .env / environment variables.

This file is complete: read it to learn the pattern.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    ollama_host: str = "http://localhost:11434"  # env: OLLAMA_HOST
    ollama_model: str = "llama3.2"  # env: OLLAMA_MODEL
    max_history_messages: int = 10  # env: MAX_HISTORY_MESSAGES
    system_prompt: str = (
        "You are a discreet, concise concierge assistant for high-net-worth clients. "
        "Answer in at most 5 sentences."
    )


@lru_cache
def get_settings() -> Settings:
    """Created once and reused, like a Spring singleton bean."""
    return Settings()
