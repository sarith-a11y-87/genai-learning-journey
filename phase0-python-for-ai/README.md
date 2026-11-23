# Phase 0: Python for AI (Sun 22 Nov – Sat 5 Dec 2026)

**Goal:** write everyday Python comfortably, then use it to call web APIs and a local LLM and serve
them through FastAPI.

**Time:** 1.5 h on weekdays and 4 h at weekends, with about 12 h a week planned.
**Pace:** one topic per day. Video first, then code straight away.

**Foundation gate (Phase 1 starts only after this):**
- [ ] 8/10 on the Day 2 self-test questions (in the study notes)
- [ ] `gate-chat-api` passes all its tests (`uv run pytest phase0-python-for-ai/gate-chat-api`)
- [ ] `gate-chat-api` works against real Ollama, and its README has a screenshot of `/docs`

## Week 1: foundations (`week1-foundations/`)

| Day | Topic | Do | Folder |
| --- | --- | --- | --- |
| Sun 22 | Core data types | Corey Schafer: strings, lists/tuples/sets, dicts. 4 Exercism exercises | `day01-collections/` |
| Mon 23 | Conditionals, loops, functions | Videos + 2 Exercism exercises | `day01-collections/` |
| Tue 24 | Comprehensions, exceptions, modules | Rewrite 3 loops as comprehensions | `day01-collections/` |
| Wed 25 | Type hints | Functions 1–2 in the Day 2 file | `day02_python_refresh.py` |
| Thu 26 | Pydantic | ArjanCodes video, functions 3–5 | `day02_python_refresh.py` |
| Fri 27 | Structured output, JSON Schema | Functions 6–7, reach **7/7** | `day02_python_refresh.py` |
| Sat 28 | Mini-project | Clients CLI with Pydantic, JSON, `.env` | `clients-cli/` |

## Week 2: APIs, async, LLMs (`week2-apis-async/`)

| Day | Topic | File |
| --- | --- | --- |
| Sun 29 | HTTP with httpx | `http_basics.py` |
| Mon 30 | asyncio | `async_basics.py` |
| Tue 1 Dec | FastAPI basics, part 1 | `fastapi_basics.py` |
| Wed 2 Dec | FastAPI basics, part 2 | `fastapi_basics.py` |
| Thu 3 Dec | Ollama from Python | `ollama_basics.py` |
| Fri 4 Dec | Buffer: catch up or rest | — |
| Sat 5 Dec | **Gate project** | `../gate-chat-api/` |

Resources for every day are in [`docs/RESOURCES.md`](../docs/RESOURCES.md).
