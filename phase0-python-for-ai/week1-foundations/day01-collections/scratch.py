"""Scratch file: type along with the videos here. Run: uv run python <path-to-this-file>"""

# Lists (like Java ArrayList)
prices = [2_500_000, 1_200_000, 4_750_000]
prices.append(980_000)
print(sorted(prices, reverse=True))

# Tuples (fixed, immutable - like a small record)
location = ("Colombo 07", 6.91, 79.86)

# Sets (unique values - like Java HashSet)
tiers = {"gold", "platinum", "gold"}  # noqa: B033 - duplicate on purpose: see it removed
print(tiers)

# Dicts (key -> value - like Java HashMap)
client = {"name": "Mr. Perera", "tier": "black", "net_worth_usd": 25_000_000}
print(client.get("email", "no email"))
