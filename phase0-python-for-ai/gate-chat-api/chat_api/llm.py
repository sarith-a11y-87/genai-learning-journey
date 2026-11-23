"""LLM access behind an interface.

Tests use a fake, and later phases can add Claude/OpenAI clients.
"""

from __future__ import annotations

from typing import Protocol

from chat_api.config import Settings
from chat_api.models import Message


class LLMClient(Protocol):
    """Anything with this method counts as an LLMClient (like a Java interface, but structural)."""

    def chat(self, messages: list[Message]) -> str: ...


class OllamaClient:
    """Real implementation using the `ollama` library. Not covered by tests - try it via /docs."""

    def __init__(self, settings: Settings) -> None:
        self.model = settings.ollama_model
        self.host = settings.ollama_host

    def chat(self, messages: list[Message]) -> str:
        """TODO:
        1. from ollama import Client  (do the import here or at the top of the file)
        2. client = Client(host=self.host)
        3. response = client.chat(model=self.model, messages=[m.model_dump() for m in messages])
        4. return response["message"]["content"]
        Bonus: catch connection errors and raise a clear RuntimeError("Is Ollama running?").
        """
        raise NotImplementedError
