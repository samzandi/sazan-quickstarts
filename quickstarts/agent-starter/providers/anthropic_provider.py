from __future__ import annotations

import os

import anthropic


class AnthropicProvider:
    """Anthropic Messages API adapter."""

    def __init__(self, model: str | None = None, max_tokens: int = 2048) -> None:
        self.model = model or os.getenv("SAZAN_MODEL", "claude-sonnet-5")
        self.max_tokens = max_tokens
        self.client = anthropic.Anthropic()

    def generate(self, prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        parts = [block.text for block in message.content if getattr(block, "type", None) == "text"]
        text = "\n".join(parts).strip()
        if not text:
            raise RuntimeError("Anthropic returned no text output.")
        return text
