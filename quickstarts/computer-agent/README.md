# Sazan Computer Agent Starter

A minimal, provider-neutral computer-use starter built around a fail-closed action policy and a credential-free simulator.

## What this starter does

- defines a small provider-neutral computer action model
- allows only `observe`, `move_pointer`, `click`, and `scroll`
- blocks text entry by default
- validates coordinates and simulated screen bounds
- runs without API keys or desktop-control privileges

## Run

```bash
cd quickstarts/computer-agent
python app.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Security boundaries

This starter intentionally does **not** control a real desktop. It does not enter credentials, handle secrets, submit forms, make purchases, change account settings, delete files, run shell commands, or perform other high-impact actions.

A real computer-control adapter should remain behind the same policy boundary and add explicit user approval for sensitive actions, sandboxing, audit logs, rate limits, recovery controls, and environment-specific authorization.

## Production status

This is a starter and simulator, not a production-ready computer-use agent. Passing tests only demonstrates the deterministic policy and simulator behavior contained in this example.
