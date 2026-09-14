# Sazan Quickstarts

A practical, provider-agnostic collection of AI agent quickstarts for building real-world applications with model providers, MCP tools, browser automation, document workflows, and business agents.

## Goals

- Fast, understandable starting points for production-minded AI projects
- Provider abstraction instead of lock-in to a single model vendor
- Security-first defaults
- Issue-driven development with evidence before declaring work done
- Reusable patterns for agents, tools, documents, browser tasks, and business workflows

## Implemented quickstarts

- `agent-starter` — minimal reusable agent foundation
- `browser-agent` — browser automation patterns
- `computer-agent` — controlled computer task simulation
- `coding-agent` — bounded coding-workspace workflow
- `customer-support-agent` — support classification and draft-response workflow
- `document-agent` — read-only document analysis workflow
- `email-agent` — bounded mailbox triage and draft workflow
- `research-agent` — citation-backed research over bounded sources
- `business-agent` — deterministic business calculations and assumption tracking
- `reviva-agent` — identity-preserving photo-restoration planning reference
- `mcp-starter` — MCP integration template

## Model providers

The repository keeps provider-specific integrations behind adapters so quickstart logic can remain portable. Provider support must be verified by each quickstart before it is claimed as tested.

## Repository validation

Run the repository-wide structural validator with:

```bash
python tools/validate_repository.py
```

The validator checks the quickstart index, required README/test structure, canonical workflow coverage, legacy duplicate workflows, and release-readiness documentation.

## Release readiness

Before any public release, review:

- `docs/RELEASE_CHECKLIST.md`
- `docs/PRE_RELEASE_READINESS.md`
- `SECURITY.md`

The first public release is blocked until the repository owner explicitly selects a license and the exact release commit has green release-relevant CI.

## Project discipline

Work should follow this lifecycle:

`Issue -> Plan -> Implementation -> Test -> Evidence -> Review -> Done`

See `START_HERE.md`, `AGENTS.md`, and `SECURITY.md` before contributing.

## Status

The quickstarts listed above are implemented and individually tested to the extent documented in their own READMEs and CI workflows. The repository as a whole is still **pre-release** and must **not** be treated as production-ready without deployment, security, failure-handling, observability, and workload-specific validation.

## Discoverability

The repository is intended to be discoverable around provider-neutral AI agents, MCP, Python agent workflows, browser automation, coding agents, document/email/research agents, security-first examples, and ReViva restoration planning. Recommended repository description and GitHub topics are recorded in `docs/PRE_RELEASE_READINESS.md` so repository settings can be applied deliberately rather than inferred.

## License

A license has not yet been selected. License selection is an explicit owner decision and is required before the first public release.
