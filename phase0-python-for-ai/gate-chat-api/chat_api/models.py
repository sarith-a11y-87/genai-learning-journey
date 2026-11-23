"""Request/response models. TODO: fill in the fields."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    """One chat message. This one is done for you."""

    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    """TODO: two fields.
    - session_id: str, 1-64 characters
    - message: str, 1-4000 characters (an empty message must be rejected with HTTP 422)
    """


class ChatResponse(BaseModel):
    """TODO: three fields.
    - session_id: str
    - reply: str
    - history_tokens: int  (estimate for the stored history AFTER this turn)
    """
