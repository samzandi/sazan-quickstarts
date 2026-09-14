# Sazan Browser Agent

A minimal, read-oriented browser automation starter built with Playwright.

## Why this starter is intentionally narrow

Browser agents can become high-impact quickly. This example does not include login flows, form submission, purchasing, file uploads, shell access, credential handling, or arbitrary cross-domain browsing. The default design is inspect-first and allowlist-driven.

## Capabilities

- open an explicitly allowed HTTP(S) page
- inspect page title, URL, and visible body text
- follow a specifically named link only when its destination remains allowed
- reject localhost, private/reserved IP targets, non-HTTP(S) schemes, and hosts outside the allowlist

## Install

```bash
cd quickstarts/browser-agent
python -m pip install -r requirements.txt
playwright install chromium
```

For Linux/CI where OS packages are also required:

```bash
playwright install --with-deps chromium
```

## Run

The default allowlist contains only `example.com`.

```bash
python app.py
```

To allow specific additional hosts, provide an explicit comma-separated list:

```bash
export SAZAN_BROWSER_ALLOWED_HOSTS=example.com,playwright.dev
python app.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

The test suite contains deterministic policy tests plus a local Chromium rendering smoke test. It does not require an API key and does not depend on an external website.

## Security boundary

Treat all web content as untrusted input. An allowlisted site can still contain prompt injection, malicious instructions, misleading UI, or links to disallowed destinations. A production browser agent should additionally use action-level authorization, sensitive-data controls, download/upload isolation, budget/rate limits, audit logs, sandboxing, and explicit human approval for consequential actions.

## Production status

This quickstart is a learning and integration foundation. It is not production-ready evidence for autonomous browsing or transactional workflows.
