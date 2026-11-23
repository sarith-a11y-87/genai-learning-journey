# Sat 28 Nov mini-project: Clients CLI

**Time:** about 3 hours. **Skills:** files, JSON, Pydantic validation, error handling, `.env` settings.

## The task

A private-banking team exports client records as JSON. Some records are broken. Build a CLI that:

1. Reads `data/clients.json` (10 made-up wealthy clients, and **3 of them are invalid on purpose**).
2. Validates each record with the Pydantic `Client` model in `clients_cli.py`.
3. Prints every invalid record with **which field failed and why**.
4. Writes `output/report.json` with, for each tier (`gold`, `platinum`, `black`), the client count
   and total net worth.
5. Reads `REPORT_CURRENCY` from your `.env` (via `pydantic-settings`) and includes it in the report.

Run it:

```bash
uv run python phase0-python-for-ai/week1-foundations/clients-cli/clients_cli.py
```

## Expected output (roughly)

```
Loaded 10 records: 7 valid, 3 invalid

INVALID record #4 (name='X'): name: String should have at least 2 characters
INVALID record #7 (name='Mr. Silva'): net_worth_usd: Input should be greater than 0
INVALID record #9 (name='Ms. Fernando'): tier: Input should be 'gold', 'platinum' or 'black'

Report written to output/report.json
```

## Done when

- [ ] All 3 invalid records are reported with the correct field
- [ ] `output/report.json` has the correct counts and totals for the 7 valid clients
- [ ] Nothing crashes if you delete a field from a record or break the JSON
- [ ] Committed and pushed. `output/` is git-ignored, which is expected.

**Stretch:** accept the file path as a command-line argument using `argparse`.
