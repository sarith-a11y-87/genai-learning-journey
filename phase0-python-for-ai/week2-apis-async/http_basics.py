"""Sun 29 Nov: HTTP with httpx (sync).

Tasks:
  1. Pick any free public JSON API that needs no key (search "free public APIs no auth").
  2. Write a Pydantic model for the fields you care about in its response.
  3. fetch_one(): GET the URL with a 10 s timeout, raise on 4xx/5xx, validate with your model.
  4. Handle httpx.TimeoutException and httpx.HTTPStatusError with a clear message.
  5. main(): call fetch_one() 5 times in a row and print the total time.
     (Tomorrow you'll make these 5 calls concurrently and compare.)

Run: uv run python phase0-python-for-ai/week2-apis-async/http_basics.py
"""

from __future__ import annotations

import time

import httpx
from pydantic import BaseModel

URL = "https://example.com/replace-with-a-real-json-api"


class Item(BaseModel):
    """TODO: fields that match the API's JSON."""


def fetch_one(client: httpx.Client) -> Item:
    """TODO:
    resp = client.get(URL)
    resp.raise_for_status()
    return Item.model_validate(resp.json())
    """
    raise NotImplementedError


def main() -> None:
    start = time.perf_counter()
    with httpx.Client(timeout=10.0) as client:
        for _ in range(5):
            print(fetch_one(client))
    print(f"5 sequential calls took {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    main()
