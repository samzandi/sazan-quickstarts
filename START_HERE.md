# START HERE

This repository is a collection of practical AI-agent quickstarts under the Sazan brand.

## Working rules

1. Start from a concrete issue or task.
2. Define acceptance criteria before implementation.
3. Prefer the smallest working change.
4. Keep model-provider logic behind adapters.
5. Never commit secrets, API keys, tokens, private credentials, or customer data.
6. Test behavior before claiming completion.
7. Record evidence for important milestones.
8. Do not call a quickstart production-ready unless deployment, security, failure handling, and observability have been validated.

## Repository map

- `quickstarts/` runnable starter projects
- `providers/` provider abstraction and adapter guidance
- `skills/` reusable agent skills and operating procedures
- `docs/` architecture and project documentation
- `examples/` focused examples and experiments

## Development loop

`Issue -> Plan -> Implement -> Test -> Evidence -> Review -> Done`

When an AI coding agent works in this repository, it must also follow `AGENTS.md`.
