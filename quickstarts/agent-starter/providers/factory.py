from __future__ import annotations

import os

from providers.anthropic_provider import AnthropicProvider
from providers.mock import MockProvider
from providers.ollama_provider import OllamaProvider
from providers.openai_provider import OpenAIProvider


def build_provider():
    name = os.getenv("SAZAN_PROVIDER", "mock").strip().lower()

    if name == "mock":
        return MockProvider()
    if name == "openai":
        return OpenAIProvider()
    if name in {"anthropic", "claude"}:
        return AnthropicProvider()
    if name == "ollama":
        return OllamaProvider()

    supported = "mock, openai, anthropic, ollama"
    raise ValueError(f"Unsupported SAZAN_PROVIDER={name!r}. Supported: {supported}")
