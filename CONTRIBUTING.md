# Contributing

Thank you for helping improve Sazan Quickstarts.

## Good contributions

Useful contributions include:

- reproducible bug reports
- security-safe fixes
- tests that expose missing behavior
- new quickstarts with a narrow, documented scope
- provider adapters that preserve the provider-neutral interface
- documentation improvements tied to verified behavior

## Before opening a pull request

1. Open or reference an issue for non-trivial work.
2. Keep the change focused.
3. Add or update tests.
4. Run the relevant quickstart tests.
5. Run `python tools/validate_repository.py`.
6. Update documentation and release notes when behavior changes.
7. Never commit credentials, private data, customer content, or production secrets.

## Pull-request expectations

A pull request should explain the problem, scope, verification performed, security implications, and any known limitations. A change is not complete only because it builds; the claimed behavior must have evidence.

## Review

Maintainers may request smaller scope, additional tests, clearer failure handling, or security changes before merge. Automated checks are necessary but do not replace maintainer review.
