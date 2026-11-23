"""Tue 1 - Wed 2 Dec: FastAPI basics.

Watch: freeCodeCamp FastAPI crash course (1 hour). Tue = first half, Wed = second half.

Run the server from the repo root:
    uv run uvicorn fastapi_basics:app --reload --app-dir phase0-python-for-ai/week2-apis-async
Then open http://127.0.0.1:8000/docs - Swagger UI is generated from your type hints.

Java/Spring mental model:
    @RestController + @GetMapping("/health")   ->   @app.get("/health")
    @RequestBody LeadDto lead                   ->   def create_lead(lead: PropertyLead)
    @PathVariable / @RequestParam               ->   function parameters
"""

from __future__ import annotations

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Phase 0 FastAPI basics")


class PropertyLead(BaseModel):
    """Same model as in day02_python_refresh.py."""

    client_name: str
    budget_usd: int = Field(gt=0)
    location: str
    bedrooms: int = Field(ge=1, le=20)
    urgency: Literal["low", "medium", "high"]


LEADS: list[PropertyLead] = []  # in-memory "database" for today


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# TODO (Tue): GET /leads/{index}  - path parameter, return 404 if out of range (HTTPException)
# TODO (Tue): GET /leads?urgency=high - query parameter that filters the list
# TODO (Wed): POST /leads - takes a PropertyLead body, appends it, returns it
# TODO (Wed): DELETE /leads/{index}
# Then try sending an invalid lead (negative budget) in /docs and read the 422 error.
