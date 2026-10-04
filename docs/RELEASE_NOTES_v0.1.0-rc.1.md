# Sazan Quickstarts v0.1.0-rc.1

Status: **pre-release; not production-ready**

This first release candidate packages the currently implemented Sazan Quickstarts together with repository-level validation, licensing documentation, community-maintenance guidance, structured contribution templates, and a dedicated release gate.

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

## Release evidence

The release candidate passed Repository Validation on Python 3.11, 3.12, and 3.13 and passed the dedicated Release Gate. The release gate resolved the current dependency set, produced an exact dependency snapshot, generated machine-readable third-party license metadata, and failed closed on missing or UNKNOWN license metadata.

The exact release target is recorded in the publication issue after the final release-candidate documentation commit and must match a green Release Gate run on `main`.

Intended tag:

`v0.1.0-rc.1`

## Open-source maintenance

The candidate includes contribution, security, maintainer, conduct, changelog, issue-template, pull-request-template, and open-source maintenance documentation. Repository validation requires these community-health files so they cannot silently disappear from the release branch.

## Licensing

The repository is licensed under Apache License 2.0. Current direct third-party dependencies and their upstream licenses are documented in `docs/THIRD_PARTY_LICENSES.md`. Release-time dependency and license evidence is produced by the Release Gate workflow.

## Safety and scope

This release candidate is intended for evaluation, experimentation, and development. It is not production-ready. Current evidence does not establish production deployment safety, internet-scale abuse resistance, complete privacy/security controls, availability objectives, observability, incident response, or workload-specific correctness.

## Publication rule

The GitHub release must be published as a pre-release, must target the exact approved commit above, and must not be presented as the latest stable release.
