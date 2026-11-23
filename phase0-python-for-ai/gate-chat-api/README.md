# Phase 0 gate project: Chat API (Sat 5 Dec 2026)

A FastAPI service that chats with a local LLM (Ollama) and remembers each conversation by session.
It is the base you'll extend in Phase 1, with streaming and cloud models, and in Phase 2, with RAG.

## What it does

```
POST /chat   {"session_id": "abc", "message": "Hi, I'm looking for a villa in Galle"}
  -> {"session_id": "abc", "reply": "...", "history_tokens": 42}

GET /health  -> {"status": "ok"}
```

- Each `session_id` has its own conversation history, kept in memory.
- Before every LLM call, the history is **trimmed** to the last `MAX_HISTORY_MESSAGES` messages,
  and the system prompt is always kept first. This is context-window management.
- `history_tokens` is a rough token estimate of the stored history (about 4 characters per token).

## Design (Java/Spring mental model)

| File | Role | Spring equivalent |
| --- | --- | --- |
| `chat_api/config.py` | Settings from `.env` (done for you) | `@ConfigurationProperties` |
| `chat_api/models.py` | Request and response models | DTOs + Bean Validation |
| `chat_api/memory.py` | `SessionStore`: per-session history | A `@Repository` (in memory) |
| `chat_api/tokens.py` | Token estimate | Utility class |
| `chat_api/llm.py` | `LLMClient` interface + `OllamaClient` | Interface + `@Service` implementation |
| `chat_api/main.py` | Routes, wired with `Depends` | `@RestController` + constructor injection |

Tests swap the real LLM for a `FakeLLM` using `app.dependency_overrides`. That's how you test without
Ollama running, the same idea as mocking a bean in Spring tests.

## How to build it (test-driven)

The tests in `tests/` are the spec. They all fail at first. Make them pass one file at a time:

```bash
uv run pytest phase0-python-for-ai/gate-chat-api/tests/test_tokens.py   # 1. easiest
uv run pytest phase0-python-for-ai/gate-chat-api/tests/test_memory.py   # 2.
uv run pytest phase0-python-for-ai/gate-chat-api/tests/test_api.py      # 3. needs models + main
uv run pytest phase0-python-for-ai/gate-chat-api                        # all green = done
```

Then `OllamaClient` in `llm.py` (no tests, because it needs a real model), and try it for real:

```bash
uv run uvicorn chat_api.main:app --reload --app-dir phase0-python-for-ai/gate-chat-api
# open http://127.0.0.1:8000/docs and chat
```

## Done when (the Phase 0 gate)

- [ ] `uv run pytest phase0-python-for-ai/gate-chat-api`: all tests pass
- [ ] Chatting through `/docs` with real Ollama works, and it remembers earlier messages
- [ ] Screenshot of `/docs` added below
- [ ] Pushed to GitHub

## Screenshot

_Add a screenshot of `/docs` here._
