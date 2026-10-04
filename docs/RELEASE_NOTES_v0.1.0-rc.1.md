# Sazan Quickstarts v0.1.0-rc.1

Status: **pre-release; not production-ready**

This first release candidate packages the implemented Sazan Quickstarts together with repository-level validation, security guidance, community-maintenance files, licensing documentation, and a dedicated fail-closed release gate.

## Included quickstarts

- agent-starter
- browser-agent
- business-agent
- coding-agent
- computer-agent
- customer-support-agent
- document-agent
- email-agent
- mcp-starter
- research-agent
- reviva-agent

## Open-source maintenance baseline

The release candidate includes:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `MAINTAINERS.md`
- `SECURITY.md`
- `CHANGELOG.md`
- structured issue templates
- a pull-request template
- `docs/OPEN_SOURCE_MAINTENANCE.md`

These files define contribution, security, maintainer, issue, pull-request, and release expectations without claiming adoption or production readiness that has not been verified.

## Release evidence

The repository validation matrix runs on Python 3.11, 3.12, and 3.13. The dedicated Release Gate validates repository structure, resolves the dependency set, records an exact dependency snapshot, generates machine-readable third-party license metadata, and fails closed on missing or UNKNOWN license metadata.

The exact release target commit and the final green workflow evidence are recorded in GitHub issue #31 immediately before publication so the release target cannot drift.

Intended tag:

`v0.1.0-rc.1`

## Licensing

The repository is licensed under Apache License 2.0. Current direct third-party dependencies and their upstream licenses are documented in `docs/THIRD_PARTY_LICENSES.md`. Release-time dependency and license evidence is produced by the Release Gate workflow.

## Safety and scope

This release candidate is intended for evaluation, experimentation, and development. It is not production-ready. Current evidence does not establish production deployment safety, internet-scale abuse resistance, complete privacy/security controls, availability objectives, observability, incident response, or workload-specific correctness.

## Publication rule

The GitHub release must be published as a pre-release, must target the exact commit recorded in issue #31 after all release-gate checks pass, and must not be presented as the latest stable release.
