# Release Checklist

Use this checklist before creating any public release or pre-release.

## Evidence and CI

- [ ] Repository Validation is green on Python 3.11, 3.12, and 3.13.
- [ ] Every quickstart-specific CI workflow required by the change is green.
- [ ] Any smoke tests documented by the affected quickstart have passed.
- [ ] No issue is marked complete without linked evidence.

## Security and scope

- [ ] `SECURITY.md` still matches the repository's actual boundaries.
- [ ] No secrets, API keys, credentials, customer data, or private assets are committed.
- [ ] Quickstarts that simulate actions clearly distinguish simulation from real execution.
- [ ] High-risk actions remain fail-closed unless explicitly reviewed and tested.
- [ ] No quickstart is described as production-ready unless deployment, security, failure handling, observability, and workload-specific validation exist.

## Documentation

- [ ] Root `README.md` accurately lists every implemented quickstart.
- [ ] `quickstarts/README.md` matches the implemented directory set.
- [ ] Each quickstart has a README and tests directory.
- [ ] Known limitations and unsupported operations are documented.
- [ ] Release notes state what changed and what remains unsupported.

## Licensing and ownership

- [ ] A repository license has been explicitly selected by the owner.
- [ ] The selected license file exists at repository root.
- [ ] Third-party code, models, SDKs, and copied assets have compatible licensing and attribution where required.

## Version and release mechanics

- [ ] Release version/tag is selected intentionally.
- [ ] The release target commit is recorded.
- [ ] Changelog/release notes reference the merged issues and PRs included in the release.
- [ ] Rollback means reverting to the previous known-good tag/commit; the exact previous reference is recorded before release.

## Final gate

A release may be published only when all required checks above are complete. If the license decision or any critical evidence is missing, the repository remains pre-release and no production-readiness claim should be made.
