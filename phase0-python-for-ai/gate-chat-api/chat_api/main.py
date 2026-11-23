"""FastAPI app. /health is done; /chat is yours.

Run: uv run uvicorn chat_api.main:app --reload --app-dir phase0-python-for-ai/gate-chat-api
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, FastAPI

from chat_api.config import Settings, get_settings
from chat_api.llm import LLMClient, OllamaClient
from chat_api.memory import SessionStore
from chat_api.models import ChatRequest, ChatResponse

app = FastAPI(title="Concierge Chat API", version="0.1.0")

_store = SessionStore()


def get_store() -> SessionStore:
    """One shared store for the whole app (tests replace it with a fresh one)."""
    return _store


def get_llm(settings: Annotated[Settings, Depends(get_settings)]) -> LLMClient:
    return OllamaClient(settings)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(
    req: ChatRequest,
    store: Annotated[SessionStore, Depends(get_store)],
    llm: Annotated[LLMClient, Depends(get_llm)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> ChatResponse:
    """TODO, in this order. Imports you will need at the top of this file:
         from chat_api.models import Message
         from chat_api.tokens import estimate_history_tokens

    1. store.add(req.session_id, "user", req.message)
    2. Build the messages for the LLM:
         [Message(role="system", content=settings.system_prompt)]
         + store.recent(req.session_id, settings.max_history_messages)
       (The system prompt is NOT stored in the session; it is added fresh on every call.)
    3. reply = llm.chat(messages)
    4. store.add(req.session_id, "assistant", reply)
    5. Return ChatResponse(session_id=..., reply=reply,
                           history_tokens=estimate_history_tokens(store.history(req.session_id)))
    """
    raise NotImplementedError
