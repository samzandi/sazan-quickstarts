from __future__ import annotations

from providers.base import ModelProvider


class Agent:
    """Small orchestration layer independent of a concrete model vendor."""

    def __init__(self, provider: ModelProvider) -> None:
        self.provider = provider

    def run(self, task: str) -> str:
        prompt = (
            "You are a careful AI assistant. Complete the user's task clearly and "
            "do not claim actions or test results that did not happen.\n\n"
            f"Task: {task.strip()}"
        )
        return self.provider.generate(prompt)
