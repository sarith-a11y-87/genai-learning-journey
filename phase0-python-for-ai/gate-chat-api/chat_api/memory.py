"""In-memory conversation history, one list of messages per session.

Phase 2+ will swap this for a database (Postgres/Redis) behind the same methods,
which is why the rest of the app only talks to SessionStore, never to the dict directly.
"""

from __future__ import annotations

from chat_api.models import Message


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, list[Message]] = {}

    def history(self, session_id: str) -> list[Message]:
        """TODO: return a COPY of the session's messages ([] for an unknown session).
        Why a copy? So callers can't accidentally change the stored history.
        """
        raise NotImplementedError

    def add(self, session_id: str, role: str, content: str) -> None:
        """TODO: append Message(role=role, content=content) to the session (create it if new)."""
        raise NotImplementedError

    def recent(self, session_id: str, max_messages: int) -> list[Message]:
        """TODO: the last `max_messages` messages of the session (all of them if fewer)."""
        raise NotImplementedError

    def clear(self, session_id: str) -> None:
        """TODO: forget a session (no error if it doesn't exist)."""
        raise NotImplementedError
