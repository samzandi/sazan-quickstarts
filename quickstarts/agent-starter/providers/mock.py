from __future__ import annotations


class MockProvider:
    """Deterministic provider used to verify the agent without external APIs."""

    def generate(self, prompt: str) -> str:
        clean = prompt.strip()
        if not clean:
            return "Please enter a task."
        return f"Sazan mock response: {clean}"
