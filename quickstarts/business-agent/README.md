# Business Agent

A minimal, provider-neutral business analysis quickstart for bounded local mock data.

## What it does
- reads only predefined local business inputs
- calculates revenue, variable cost, contribution margin, operating result, and break-even units deterministically
- records assumptions explicitly
- refuses unsupported analysis when inputs are invalid, unknown, or cannot produce a meaningful break-even result

## Safety boundaries
This demo does **not** access live accounts, payment systems, bank data, external APIs, the network, or arbitrary files. It does not make purchases, move money, execute shell commands, provide legal advice, or provide tax advice.

## Run locally
```bash
cd quickstarts/business-agent
python app.py
python -m unittest discover -s tests -v
```

## Status
Educational quickstart only. It is not production-ready and has not been validated for real financial decisions, accounting standards, taxes, forecasting, authentication, privacy, or live integrations.
