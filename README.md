# Sazan Quickstarts

[![Repository Validation](https://github.com/samzandi/sazan-quickstarts/actions/workflows/repository-validation.yml/badge.svg)](https://github.com/samzandi/sazan-quickstarts/actions/workflows/repository-validation.yml)
[![Release Gate](https://github.com/samzandi/sazan-quickstarts/actions/workflows/release-gate.yml/badge.svg)](https://github.com/samzandi/sazan-quickstarts/actions/workflows/release-gate.yml)
[![GitHub release](https://img.shields.io/github/v/release/samzandi/sazan-quickstarts?include_prereleases)](https://github.com/samzandi/sazan-quickstarts/releases)
[![License](https://img.shields.io/github/license/samzandi/sazan-quickstarts)](LICENSE)

A practical, provider-agnostic collection of AI agent quickstarts for building real-world applications with model providers, MCP tools, browser automation, document workflows, and business agents.

## Quick start

Clone the repository and run the credential-free starter:

```bash
git clone https://github.com/samzandi/sazan-quickstarts.git
cd sazan-quickstarts/quickstarts/agent-starter
python app.py
```

The default provider is `mock`, so the first run does not require an API key. Each quickstart documents its own provider, security, and validation requirements.

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

The validator checks the quickstart index, required README/test structure, canonical workflow coverage, legacy duplicate workflows, release-readiness documentation, and the selected repository license.

## Releases

The first public release candidate is available as [v0.1.0-rc.1](https://github.com/samzandi/sazan-quickstarts/releases/tag/v0.1.0-rc.1).

Release publication is guarded by repository validation, dependency/license evidence, and a dedicated fail-closed Release Gate. See:

- `docs/RELEASE_CHECKLIST.md`
- `docs/PRE_RELEASE_READINESS.md`
- `docs/RELEASE_NOTES_v0.1.0-rc.1.md`
- `SECURITY.md`

## Project discipline

Work follows this lifecycle:

`Issue -> Plan -> Implementation -> Test -> Evidence -> Review -> Done`

See `START_HERE.md`, `AGENTS.md`, and `SECURITY.md` before contributing.

## Status

The quickstarts listed above are implemented and individually tested to the extent documented in their own READMEs and CI workflows. The repository is in **pre-1.0 development** and must **not** be treated as production-ready without deployment, security, failure-handling, observability, and workload-specific validation.

## Discoverability

The repository is intended to be discoverable around provider-neutral AI agents, MCP, Python agent workflows, browser automation, coding agents, document/email/research agents, security-first examples, and ReViva restoration planning. Recommended repository description and GitHub topics are recorded in `docs/PRE_RELEASE_READINESS.md`.

## License

Licensed under the Apache License, Version 2.0. See `LICENSE` for the full license text.

## Open-source maintenance

Sazan Quickstarts is actively maintained as a public open-source project. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements, [SECURITY.md](SECURITY.md) for vulnerability reporting, [MAINTAINERS.md](MAINTAINERS.md) for maintainer responsibilities, and [docs/OPEN_SOURCE_MAINTENANCE.md](docs/OPEN_SOURCE_MAINTENANCE.md) for the maintenance and release model.

Repository activity is evidence-driven: issues, pull requests, tests, and releases should reflect real work. The project does not claim adoption, production readiness, or usage metrics that have not been verified.
