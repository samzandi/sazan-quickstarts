from __future__ import annotations

from typing import Protocol


class ModelProvider(Protocol):
    """Minimal interface implemented by every model provider adapter."""

    def generate(self, prompt: str) -> str:
        """Return a model response for a single prompt."""
        ...
