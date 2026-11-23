"""Mon 30 Nov: asyncio + httpx.AsyncClient.

Watch first: Tech With Tim, "Python Asynchronous Programming - AsyncIO and Async-Await".

Tasks:
  1. Copy your Item model and URL from http_basics.py.
  2. fetch_one(): the async version, using `await client.get(...)`.
  3. main(): run 5 calls at once with asyncio.gather and print the total time.
  4. In docs/notes/week02.md, compare the sequential and concurrent timings and explain WHY
     the concurrent version is faster (hint: what is the program doing while it waits?).

Java mental model: asyncio.gather is like CompletableFuture.allOf, but on ONE thread.

Run: uv run python phase0-python-for-ai/week2-apis-async/async_basics.py
"""

from __future__ import annotations

import asyncio
import time

import httpx


async def fetch_one(client: httpx.AsyncClient) -> dict:
    """TODO: await client.get(URL), raise for status, return resp.json() (or your Item model)."""
    raise NotImplementedError


async def main() -> None:
    start = time.perf_counter()
    async with httpx.AsyncClient(timeout=10.0) as client:
        results = await asyncio.gather(*(fetch_one(client) for _ in range(5)))
    print(f"{len(results)} concurrent calls took {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
