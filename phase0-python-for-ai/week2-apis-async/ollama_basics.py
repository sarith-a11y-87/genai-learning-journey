"""Thu 3 Dec: talk to a local LLM with the Ollama Python library.

Before you start: Ollama is running and you've pulled a model: `ollama pull llama3.2`
Reference: https://github.com/ollama/ollama-python

Tasks:
  1. one_shot(): send one user message, print the reply.
  2. streaming(): same, but stream=True, printing each chunk as it arrives (end="", flush=True).
  3. conversation(): a 3-turn chat. Keep a messages list, append the assistant's reply after
     each turn, and show that the model remembers turn 1 in turn 3.
  4. Try temperature 0 vs 1 (options={"temperature": ...}) on the same prompt;
     note the difference.

Run: uv run python phase0-python-for-ai/week2-apis-async/ollama_basics.py
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def one_shot() -> None:
    """TODO: ollama.chat(model=MODEL, messages=[{"role": "user", "content": "..."}])."""
    raise NotImplementedError


def streaming() -> None:
    """TODO: same as one_shot, with stream=True."""
    raise NotImplementedError


def conversation() -> None:
    """TODO: 3 turns, keeping the full message history."""
    raise NotImplementedError


if __name__ == "__main__":
    one_shot()
    streaming()
    conversation()
