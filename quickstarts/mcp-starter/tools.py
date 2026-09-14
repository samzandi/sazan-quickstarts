from __future__ import annotations

from collections.abc import Callable
from typing import Any


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def health() -> dict[str, str]:
    """Return a small health payload for smoke checks."""
    return {"status": "ok", "service": "sazan-mcp-starter"}


# Explicit allowlist. Adding a function to this module does not expose it automatically.
SAFE_TOOLS: tuple[Callable[..., Any], ...] = (add, health)
