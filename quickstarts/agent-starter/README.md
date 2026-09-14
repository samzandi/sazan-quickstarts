# Agent Starter

Minimal provider-agnostic foundation for a Sazan AI agent.

## What it demonstrates

- a stable provider interface;
- separation between agent logic and model-vendor code;
- a zero-secret mock provider for local verification;
- a small command-line loop that can later be connected to OpenAI, Anthropic, Ollama, or another adapter.

## Run

```bash
python app.py
```

No API key is required for the default mock provider.

## Architecture

- `app.py` — CLI entry point
- `agent.py` — agent orchestration
- `providers/base.py` — provider protocol
- `providers/mock.py` — local deterministic provider

## Status

This starter is intentionally minimal. It is suitable as an architecture seed, not as a production agent.
