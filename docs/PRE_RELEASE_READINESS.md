# Pre-release Readiness

Status: **pre-release; not production-ready**

This document records repository-level readiness evidence and explicit blockers before the first public release.

## Implemented scope

The repository currently contains these implemented quickstarts:

- `agent-starter`
- `browser-agent`
- `computer-agent`
- `coding-agent`
- `customer-support-agent`
- `document-agent`
- `email-agent`
- `research-agent`
- `business-agent`
- `reviva-agent`
- `mcp-starter`

Each quickstart has a canonical CI workflow and repository validation checks the expected structure.

## Repository-level evidence

- Repository-wide structural validation exists under `tools/validate_repository.py`.
- Validation runs on Python 3.11, 3.12, and 3.13.
- Duplicate legacy workflows for Agent Starter and MCP Starter were removed.
- The canonical MCP workflow retains its server import smoke check.
- Root and quickstart indexes reflect implemented examples rather than planned-only status.
- The repository owner explicitly selected Apache-2.0 and the canonical full license text is stored in `LICENSE`.

## Explicit blockers before first public release

1. **Release version/tag** — must be selected intentionally at release time.
2. **Final CI snapshot** — all release-relevant checks must be green on the exact release commit.
3. **Third-party licensing review** — dependencies, SDKs, models, and any copied assets must be checked for compatibility and attribution requirements.

## Not established by current evidence

Current CI does **not** establish production readiness. It does not prove production deployment safety, internet-scale abuse resistance, complete privacy/security controls, availability targets, observability, incident response, or workload-specific correctness.

## Repository discoverability guidance

Recommended repository description:

`Security-first, provider-neutral AI agent quickstarts with tested examples for browser, coding, documents, email, research, business workflows, MCP, and ReViva.`

Recommended GitHub topics:

`ai-agents`, `agentic-ai`, `mcp`, `python`, `llm`, `browser-automation`, `developer-tools`, `ai-workflows`, `security`, `quickstart`

These repository settings should be applied only through an authorized repository-settings action; documentation alone does not claim they are already configured.
