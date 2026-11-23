"""Rough token estimate. Real tokenizers come in Phase 1."""

from __future__ import annotations

from chat_api.models import Message


def estimate_tokens(text: str) -> int:
    """TODO: about 4 characters per token, rounded UP. Empty string -> 0. (Same as Day 2.)"""
    raise NotImplementedError


def estimate_history_tokens(messages: list[Message]) -> int:
    """TODO: sum estimate_tokens over every message's content."""
    raise NotImplementedError
