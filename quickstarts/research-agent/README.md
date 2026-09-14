# Research Agent

A minimal, provider-neutral research quickstart focused on bounded evidence, explicit source IDs, and refusal of unsupported claims.

## What it does
- searches a small local mock source corpus
- ranks matches deterministically
- returns findings with explicit source IDs
- refuses to invent an answer when evidence is missing

## Safety boundaries
This demo has no live web access, shell execution, credentials, arbitrary filesystem access, external API calls, or autonomous publishing. It does not treat missing evidence as permission to guess.

## Run locally
```bash
cd quickstarts/research-agent
python app.py
python -m unittest discover -s tests -v
```

## Status
Educational quickstart only. It is not production-ready and has not been hardened for adversarial sources, prompt injection, provenance verification, source freshness, conflict resolution, privacy, rate limiting, observability, or live retrieval integrations.
