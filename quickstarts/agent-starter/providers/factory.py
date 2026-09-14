from __future__ import annotations

import os

from providers.mock import MockProvider


def build_provider():
    """Build a provider from environment configuration using lazy imports."""
    name = os.getenv("SAZAN_PROVIDER", "mock").strip().lower()

    if name == "mock":
        return MockProvider()
    if name == "openai":
        from providers.openai_provider import OpenAIProvider

        return OpenAIProvider()
    if name in {"anthropic", "claude"}:
        from providers.anthropic_provider import AnthropicProvider

        return AnthropicProvider()
    if name == "ollama":
        from providers.ollama_provider import OllamaProvider

        return OllamaProvider()

    supported = "mock, openai, anthropic, ollama"
    raise ValueError(f"Unsupported SAZAN_PROVIDER={name!r}. Supported: {supported}")
