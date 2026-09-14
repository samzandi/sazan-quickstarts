from __future__ import annotations

import os

from openai import OpenAI


class OpenAIProvider:
    """OpenAI Responses API adapter."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("SAZAN_MODEL", "gpt-5.6")
        self.client = OpenAI()

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        text = response.output_text
        if not text:
            raise RuntimeError("OpenAI returned no text output.")
        return text
