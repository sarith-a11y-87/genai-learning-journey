"""
Day 02 - Python refresh for AI engineering
Phase 0, Week 1 (Wed 25 - Fri 27 Nov 2026)

How to use this file:
  1. Work through it over Wed 25 - Fri 27 Nov (see the phase README).
  2. Fill in every function marked TODO (replace `raise NotImplementedError`).
  3. Run it:  uv run python phase0-python-for-ai/week1-foundations/day02_python_refresh.py
  4. When every check prints PASS, commit and push.

Why these topics? Almost every AI library (Anthropic/OpenAI SDKs, LangChain,
LangGraph, FastAPI) is built on TYPE HINTS and PYDANTIC. Pydantic is also how
you force an LLM to return clean, validated JSON, and how tool/function
schemas are written for agents.

Setup: already installed by `uv sync` at the repo root.
"""

from __future__ import annotations

import json
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

# ---------------------------------------------------------------------------
# PART 1 - Type hints (Java habit -> Python syntax)
# Java:   public int countTokens(String text)
# Python: def count_tokens(text: str) -> int:
# ---------------------------------------------------------------------------


def estimate_tokens(text: str) -> int:
    """
    TODO: Rough token estimate. A common rule of thumb for English is
    ~4 characters per token. Return ceil(len(text) / 4).
    Empty string -> 0.
    Hint: use math.ceil, or the integer trick  -(-a // b)
    """
    raise NotImplementedError


def estimate_cost_usd(
    input_tokens: int, output_tokens: int, input_price_per_m: float, output_price_per_m: float
) -> float:
    """
    TODO: LLM APIs charge per MILLION tokens, separately for input and output.
    cost = input_tokens/1_000_000 * input_price + output_tokens/1_000_000 * output_price
    Return the cost rounded to 6 decimal places.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART 2 - Pydantic models (think: a Java DTO + Bean Validation in one class)
# This is the exact shape of a chat message in every LLM API.
# ---------------------------------------------------------------------------


class Message(BaseModel):
    # Literal = only these exact values are allowed (like a Java enum)
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)


class Conversation(BaseModel):
    messages: list[Message] = Field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        """TODO: create a Message and append it to self.messages."""
        raise NotImplementedError

    def total_tokens(self) -> int:
        """TODO: sum estimate_tokens() over every message's content."""
        raise NotImplementedError

    def last_n(self, n: int) -> list[Message]:
        """
        TODO: return the last n messages, BUT always keep the system message
        (if the first message is a system message) at the front.
        This is the simplest form of 'context window management'.
        Example: [sys, u1, a1, u2, a2], n=2 -> [sys, u2, a2]
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# PART 3 - Validating LLM output (structured output)
# LLMs return TEXT. You ask for JSON, then validate it with Pydantic so bad
# output fails loudly instead of breaking your app later.
# ---------------------------------------------------------------------------


class PropertyLead(BaseModel):
    """Imagine an LLM extracted this from a luxury real-estate enquiry email."""

    client_name: str
    budget_usd: int = Field(gt=0)
    location: str
    bedrooms: int = Field(ge=1, le=20)
    urgency: Literal["low", "medium", "high"]


def parse_lead(raw_llm_output: str) -> PropertyLead | None:
    """
    TODO: Parse the raw JSON string into a PropertyLead.
    - Valid JSON + valid fields  -> return the PropertyLead
    - Invalid JSON or failed validation -> return None (do NOT crash)
    Hint: PropertyLead.model_validate_json(raw) raises ValidationError on
    bad JSON or bad fields.
    """
    raise NotImplementedError


def lead_schema() -> dict:
    """
    TODO: Return the JSON Schema of PropertyLead.
    Hint: one method call on the class. This dict is EXACTLY what you pass to
    an LLM as a tool / function definition in Week 3 (agents).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Self-checks - don't edit below. Run the file; aim for all PASS.
# ---------------------------------------------------------------------------


def _check(name: str, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except NotImplementedError:
        print(f"TODO  {name}")
    except AssertionError as e:
        print(f"FAIL  {name}  {e}")
    except Exception as e:  # noqa: BLE001
        print(f"ERROR {name}  {type(e).__name__}: {e}")
    return False


def _t1():
    assert estimate_tokens("") == 0
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("abcde") == 2
    assert estimate_tokens("Hello, world!") == 4


def _t2():
    # 2,000 in + 500 out at $3 / $15 per million
    assert estimate_cost_usd(2_000, 500, 3.0, 15.0) == 0.0135
    assert estimate_cost_usd(0, 0, 3.0, 15.0) == 0.0


def _t3():
    c = Conversation()
    c.add("system", "You are a concierge.")
    c.add("user", "Book a table.")
    assert len(c.messages) == 2 and c.messages[1].role == "user"
    try:
        c.add("robot", "hi")
        raise AssertionError("role 'robot' should be rejected")
    except ValidationError:
        pass


def _t4():
    c = Conversation()
    c.add("user", "abcd")
    c.add("assistant", "abcdefgh")
    assert c.total_tokens() == 3


def _t5():
    c = Conversation()
    for role, text in [
        ("system", "S"),
        ("user", "u1"),
        ("assistant", "a1"),
        ("user", "u2"),
        ("assistant", "a2"),
    ]:
        c.add(role, text)
    assert [m.content for m in c.last_n(2)] == ["S", "u2", "a2"]
    c2 = Conversation()
    for role, text in [("user", "u1"), ("assistant", "a1"), ("user", "u2")]:
        c2.add(role, text)
    assert [m.content for m in c2.last_n(2)] == ["a1", "u2"]


def _t6():
    good = json.dumps(
        {
            "client_name": "Mr. Perera",
            "budget_usd": 2_500_000,
            "location": "Colombo 07",
            "bedrooms": 4,
            "urgency": "high",
        }
    )
    lead = parse_lead(good)
    assert lead is not None and lead.bedrooms == 4
    assert parse_lead('{"client_name": "X"') is None  # broken JSON
    bad = json.dumps(
        {
            "client_name": "X",
            "budget_usd": -5,
            "location": "Galle",
            "bedrooms": 3,
            "urgency": "high",
        }
    )
    assert parse_lead(bad) is None  # negative budget
    assert parse_lead(good.replace('"high"', '"ASAP"')) is None  # bad enum


def _t7():
    s = lead_schema()
    assert s["type"] == "object"
    assert set(s["required"]) == {"client_name", "budget_usd", "location", "bedrooms", "urgency"}


if __name__ == "__main__":
    checks = [
        ("1 estimate_tokens", _t1),
        ("2 estimate_cost_usd", _t2),
        ("3 Conversation.add + validation", _t3),
        ("4 Conversation.total_tokens", _t4),
        ("5 Conversation.last_n (context window)", _t5),
        ("6 parse_lead (structured output)", _t6),
        ("7 lead_schema (tool schema)", _t7),
    ]
    passed = sum(_check(n, f) for n, f in checks)
    print(f"\n{passed}/{len(checks)} passed")
    if passed == len(checks):
        print("Day 02 complete - commit and push!")
