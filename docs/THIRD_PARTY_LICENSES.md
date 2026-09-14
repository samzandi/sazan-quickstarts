# Third-Party License Review

Review date: 2026-09-14

This document records the direct Python dependencies currently declared by `sazan-quickstarts`, their upstream licensing, compatibility notes, and release-time follow-up requirements. It is a repository engineering record, not legal advice.

## Direct dependencies

| Dependency | Declared range | Used by | Upstream license | Upstream source | Repository action |
| --- | --- | --- | --- | --- | --- |
| `openai` | `>=1.0.0` | `agent-starter` | Apache-2.0 in the current official SDK metadata | https://github.com/openai/openai-python | Compatible with this repository's Apache-2.0 license at the direct-dependency level. Preserve upstream license/notice obligations when redistributing upstream code rather than merely depending on the package. |
| `anthropic` | `>=0.40.0` | `agent-starter` | MIT | https://github.com/anthropics/anthropic-sdk-python | Permissive dependency. Preserve MIT copyright/license notice if upstream code is copied or redistributed as required by its license. |
| `playwright` | `>=1.55,<2` | `browser-agent` | Apache-2.0 | https://github.com/microsoft/playwright-python | Compatible with this repository's Apache-2.0 license at the direct-dependency level. Preserve applicable attribution/NOTICE material if redistributed. |
| `mcp[cli]` | `>=2,<3` | `mcp-starter` | MIT | https://github.com/modelcontextprotocol/python-sdk | Permissive dependency. Preserve MIT copyright/license notice if upstream code is copied or redistributed as required by its license. |

## Findings

- No direct dependency currently reviewed here presents an obvious license conflict with the repository's Apache-2.0 license.
- The repository currently depends on packages by reference through `requirements.txt`; it does not vendor the reviewed SDK source code.
- No third-party model weights, datasets, fonts, media assets, or copied third-party source files were identified as part of this direct dependency inventory.
- License status can change between major package versions. The ranges in this repository are not fully pinned, so this review is evidence for the currently inspected upstream projects, not a permanent guarantee for every future resolved package version.

## Transitive dependencies

This document does **not** claim a complete transitive dependency license audit. Packages such as HTTP clients, validation libraries, browser-support packages, CLI dependencies, and their own dependency trees are resolved by package installation and may vary over time because the direct requirements are ranges rather than a lockfile.

Before the first public pre-release:

1. Resolve the exact release dependency set on the exact release commit.
2. Record the resolved versions (lockfile or equivalent reproducible snapshot).
3. Generate or inspect a transitive license inventory for that resolved set.
4. Investigate any copyleft, source-available, unknown, custom, or missing-license result before release.
5. Preserve required notices/attributions in the release if any resolved dependency requires them.

## Release gate

The direct-dependency review is complete for the dependencies currently declared in this repository. The remaining licensing gate is the **resolved transitive dependency snapshot and attribution check on the exact release candidate**.

Any new direct dependency, vendored code, model, dataset, font, image, audio, or other third-party asset must be added to this review before a release that includes it.
