"""Shared test setup: makes `chat_api` importable and swaps in a fake LLM + fresh store."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_DIR = Path(__file__).resolve().parents[1]
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from chat_api.config import Settings, get_settings  # noqa: E402
from chat_api.main import app, get_llm, get_store  # noqa: E402
from chat_api.memory import SessionStore  # noqa: E402
from chat_api.models import Message  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402


class FakeLLM:
    """Replies 'echo: <last user message>' and records what it was sent."""

    def __init__(self) -> None:
        self.calls: list[list[Message]] = []

    def chat(self, messages: list[Message]) -> str:
        self.calls.append(list(messages))
        return f"echo: {messages[-1].content}"


@pytest.fixture
def fake_llm() -> FakeLLM:
    return FakeLLM()


@pytest.fixture
def settings() -> Settings:
    return Settings(max_history_messages=4, system_prompt="TEST SYSTEM PROMPT")


@pytest.fixture
def client(fake_llm: FakeLLM, settings: Settings):
    store = SessionStore()
    app.dependency_overrides[get_llm] = lambda: fake_llm
    app.dependency_overrides[get_store] = lambda: store
    app.dependency_overrides[get_settings] = lambda: settings
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
