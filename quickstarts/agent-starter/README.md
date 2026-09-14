# Sazan Agent Starter

A minimal provider-neutral AI agent starter.

## Supported providers

- `mock` — no API key, useful for local smoke tests
- `openai` — OpenAI Responses API
- `anthropic` / `claude` — Anthropic Messages API
- `ollama` — local Ollama HTTP API

## Run

```bash
cd quickstarts/agent-starter
python app.py
```

The default provider is `mock`, so the starter runs without credentials.

## Cloud setup

Copy `.env.example` values into your shell environment or secret manager. Do not commit real credentials.

OpenAI example:

```bash
export SAZAN_PROVIDER=openai
export OPENAI_API_KEY=your_key_here
export SAZAN_MODEL=gpt-5.6
python app.py
```

Anthropic example:

```bash
export SAZAN_PROVIDER=anthropic
export ANTHROPIC_API_KEY=your_key_here
export SAZAN_MODEL=claude-sonnet-5
python app.py
```

Ollama example:

```bash
export SAZAN_PROVIDER=ollama
export SAZAN_MODEL=llama3.2
python app.py
```

## Architecture

- `app.py` — CLI entry point
- `agent.py` — provider-independent orchestration
- `providers/base.py` — provider protocol
- `providers/factory.py` — environment-driven provider selection
- `providers/mock.py` — local deterministic provider
- `providers/openai_provider.py` — OpenAI adapter
- `providers/anthropic_provider.py` — Anthropic adapter
- `providers/ollama_provider.py` — Ollama adapter

## Tests

```bash
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same test suite for relevant pushes and pull requests.

## Production status

This starter is intentionally small. Passing starter tests is evidence that the local orchestration path works; it is not evidence that a deployment is production-ready. Provider credentials, rate limits, retries, observability, cost controls, security review, and deployment-specific tests remain required.
