# Quickstarts

Each directory in this folder should be independently understandable and testable.

## Implemented

- `agent-starter`
- `browser-agent`
- `business-agent`
- `coding-agent`
- `computer-agent`
- `customer-support-agent`
- `document-agent`
- `email-agent`
- `mcp-starter`
- `research-agent`
- `reviva-agent`

## Structural requirements

Every implemented quickstart must include:

- its own `README.md`
- a `tests/` directory with deterministic tests
- a canonical workflow at `.github/workflows/<quickstart>.yml`
- explicit security/safety boundaries
- a clear statement of what has actually been tested
- no production-ready claim without deployment, security, failure-handling, and observability evidence

Repository-wide consistency is checked by `tools/validate_repository.py` and the `Repository Validation` workflow.
