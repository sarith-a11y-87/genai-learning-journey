"""Sat 28 Nov mini-project: Clients CLI. See README.md in this folder for the task.

Run from the repo root:
    uv run python phase0-python-for-ai/week1-foundations/clients-cli/clients_cli.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

HERE = Path(__file__).parent
DATA_FILE = HERE / "data" / "clients.json"
OUTPUT_FILE = HERE / "output" / "report.json"


class Settings(BaseSettings):
    """Reads values from the .env file at the repo root (and from environment variables)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    report_currency: str = "USD"


class Client(BaseModel):
    """TODO: add the fields. Look at data/clients.json for the shape.

    Rules:
      - name: at least 2 characters
      - net_worth_usd: integer greater than 0
      - tier: only "gold", "platinum" or "black"
      - email: optional (can be null)
      - city: string
    """

    # Example of one field so you can see the pattern:
    name: str = Field(min_length=2)
    # TODO: net_worth_usd, tier (use Literal), email, city


TIERS: tuple[Literal["gold", "platinum", "black"], ...] = ("gold", "platinum", "black")


def load_raw_records(path: Path) -> list[dict]:
    """TODO: read the JSON file and return the list of dicts.
    Handle a missing file or broken JSON with a clear message instead of a crash.
    """
    raise NotImplementedError


Invalid = tuple[int, dict, ValidationError]  # (record_number, raw_dict, error)


def validate_records(raw: list[dict]) -> tuple[list[Client], list[Invalid]]:
    """TODO: return (valid_clients, invalid) where invalid holds (record_number, raw_dict, error).
    Record numbers start at 1. Hint: Client.model_validate(d) inside try/except ValidationError.
    """
    raise NotImplementedError


def build_report(clients: list[Client], currency: str) -> dict:
    """TODO: return a dict like
    {
      "currency": "USD",
      "total_clients": 7,
      "by_tier": {
        "gold": {"count": 2, "total_net_worth": 5950000},
        "platinum": {...},
        "black": {...}
      }
    }
    Tip: a dict comprehension over TIERS is a clean way to build "by_tier".
    """
    raise NotImplementedError


def main() -> None:
    settings = Settings()
    raw = load_raw_records(DATA_FILE)
    valid, invalid = validate_records(raw)
    print(f"Loaded {len(raw)} records: {len(valid)} valid, {len(invalid)} invalid\n")

    for number, record, error in invalid:
        first = error.errors()[0]
        field = ".".join(str(p) for p in first["loc"])
        print(f"INVALID record #{number} (name={record.get('name')!r}): {field}: {first['msg']}")

    report = build_report(valid, settings.report_currency)
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2))
    print(f"\nReport written to {OUTPUT_FILE.relative_to(HERE)}")


if __name__ == "__main__":
    main()
