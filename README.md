# GenAI Learning Journey: RAG, AI Agents and Agentic AI

My 6-month path from Java/Spring Boot backend engineer to AI engineer who can ship
production RAG systems and AI agents. **22 Nov 2026 – 21 May 2027**, at 12–15 hours a week.

**Author:** Sarith Ranathunge, Associate Full-Stack Engineer (Java, Spring Boot, React)

## Roadmap

| Dates | Phase | Folder | Gate (proof of skill) |
| --- | --- | --- | --- |
| 22 Nov – 5 Dec | 0. Python for AI | [`phase0-python-for-ai`](phase0-python-for-ai/) | FastAPI chat service that calls a local LLM |
| 6 Dec – 25 Dec | 1. Generative AI foundations | [`phase1-genai-foundations`](phase1-genai-foundations/) | CLI chatbot with memory, streaming and a cost counter |
| 26 Dec – 1 Jan | Break | — | — |
| 2 Jan – 29 Jan | 2. RAG | [`phase2-rag`](phase2-rag/) | Private Wealth Document Assistant with an eval report |
| 30 Jan – 26 Feb | 3. AI agents | [`phase3-agents`](phase3-agents/) | Investment Research Agent with your own MCP server |
| 27 Feb – 2 Apr | 4. Agentic AI in production | [`phase4-agentic-systems`](phase4-agentic-systems/) | Multi-agent Executive Concierge, deployed |
| 3 Apr – 21 May | 5. Advanced work | [`phase5-advanced`](phase5-advanced/) | Spring AI rebuild, fine-tuning, articles |

Rules I follow: **foundations before advanced**, one topic a day, code every day, and no
moving on to the next phase until its gate project works and is pushed.

## Progress

### Certificates

- [x] Google Cloud: Generative AI Fundamentals skill badge
- [ ] Databricks: Generative AI Fundamentals
- [ ] Claude Academy: Building with the Claude API
- [ ] Hugging Face: AI Agents Course (fundamentals certificate)
- [ ] Hugging Face: AI Agents Course (full certificate)

### Phase gates

- [ ] Phase 0: FastAPI chat service (`phase0-python-for-ai/gate-chat-api`)
- [ ] Phase 1: CLI chatbot
- [ ] Phase 2: Private Wealth Document Assistant
- [ ] Phase 3: Investment Research Agent
- [ ] Phase 4: Executive Concierge
- [ ] Phase 5: Spring AI rebuild

The daily log lives in [`docs/PROGRESS.md`](docs/PROGRESS.md), and my study notes are in [`docs/notes/`](docs/notes/).

## Setup

You need **Python 3.12+**, **[uv](https://docs.astral.sh/uv/)**, **Git** and **[Ollama](https://ollama.com)**, which provides free local LLMs.

```bash
git clone https://github.com/<your-username>/genai-learning-journey.git
cd genai-learning-journey
uv sync                       # creates .venv and installs everything
cp .env.example .env          # then fill in values (never commit .env)
ollama pull llama3.2          # one-time model download (~2 GB)
```

Everyday commands:

```bash
uv run python path/to/file.py          # run a script
uv run pytest                          # run all tests
uv run pytest phase0-python-for-ai/gate-chat-api   # run one project's tests
uv run ruff check .                    # lint
uv run ruff format .                   # auto-format
```

## Repository layout

```
genai-learning-journey/
├── docs/                      # roadmap, progress log, study notes
├── phase0-python-for-ai/
│   ├── week1-foundations/     # collections, functions, type hints, Pydantic
│   ├── week2-apis-async/      # httpx, asyncio, FastAPI, Ollama
│   └── gate-chat-api/         # Phase 0 gate project (with tests)
├── phase1-genai-foundations/
├── phase2-rag/
├── phase3-agents/
├── phase4-agentic-systems/
├── phase5-advanced/
└── projects/                  # the 4 portfolio projects (each later gets its own repo)
```

## Commit style

One commit per finished task, with a clear message:

```
feat(phase0): solve day02 pydantic exercises (7/7)
docs(notes): week1 notes on collections
fix(gate): trim history before calling the LLM
```

## License

MIT. See [LICENSE](LICENSE).
