# AGENTS

Instructions for AI agents working in this repository.

## Core behavior

- Read `START_HERE.md` before making changes.
- Work issue-first whenever practical.
- Preserve existing architecture unless a change is justified.
- Prefer explicit, inspectable code over opaque automation.
- Keep provider-specific code isolated behind adapters.
- Do not fabricate test results, deployment status, benchmarks, or evidence.

## Definition of done

A task is complete only when:

- requested behavior is implemented;
- relevant tests or checks pass;
- failure cases are considered;
- secrets are not exposed;
- documentation is updated when behavior changes;
- evidence is available for material claims.

## Safety

Never commit:

- API keys or access tokens;
- passwords or private keys;
- production customer data;
- private email content;
- environment files containing secrets.

Use `.env.example` files with placeholders only.

## Change discipline

For non-trivial work:

1. reference an issue;
2. state acceptance criteria;
3. implement narrowly;
4. test;
5. record evidence;
6. open a pull request when review is useful.
