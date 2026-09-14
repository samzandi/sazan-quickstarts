# Document Agent

A minimal, provider-neutral document quickstart focused on read-only, grounded responses.

## What it does
- selects a document by an explicit local document ID
- returns metadata, a deterministic summary, or a grounded answer
- attaches a source ID to grounded outputs
- falls back when requested information is not present

## Safety boundaries
This demo is intentionally read-only. It does **not** modify source documents, read arbitrary filesystem paths, call external networks, run shell commands, execute embedded document content, or handle credentials/secrets.

The demo store contains only in-code mock text. Real PDF/DOCX parsing, OCR, uploads, authentication, privacy controls, malware scanning, prompt-injection defenses, rate limiting, and observability are out of scope.

## Run locally
```bash
cd quickstarts/document-agent
python app.py
python -m unittest discover -s tests -v
```

## Status
Educational quickstart only. It is not production-ready.
