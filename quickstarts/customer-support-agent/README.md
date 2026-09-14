# Customer Support Agent

A minimal, provider-neutral customer support quickstart focused on safe routing and bounded answers.

## What it does
- classifies a request deterministically in demo mode
- answers only from a small local knowledge base
- attaches a source ID to every answered FAQ
- escalates unsupported or sensitive requests

## Safety boundaries
This demo does **not** perform account changes, refunds, payments, credential handling, external API calls, legal advice, medical advice, or destructive actions. Unknown requests are escalated instead of guessed.

## Run locally
```bash
cd quickstarts/customer-support-agent
python app.py
python -m unittest discover -s tests -v
```

## Status
Educational quickstart only. It is not production-ready and has not been hardened for real customer data, authentication, privacy requirements, rate limiting, observability, or live integrations.
