from __future__ import annotations


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def health() -> dict[str, str]:
    """Return a small health payload for smoke checks."""
    return {"status": "ok", "service": "sazan-mcp-starter"}
