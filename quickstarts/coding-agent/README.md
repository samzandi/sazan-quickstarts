# Sazan Coding Agent

A minimal, provider-neutral coding-agent foundation focused on safe workspace inspection and explicitly approved file edits.

## Capabilities

- list files inside one configured workspace root
- read UTF-8 text files inside that workspace
- preview proposed changes as a unified diff
- write files only after explicit approval
- run entirely locally without API keys

## Intentionally excluded

This starter does **not** execute shell commands, install packages, access the network, handle credentials, modify Git history, delete files, or perform repository-wide destructive actions.

## Run the local demo

```bash
cd quickstarts/coding-agent
python app.py
```

The demo creates a temporary workspace, previews a change, and intentionally does not apply the write.

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests verify workspace confinement, path-traversal blocking, preview-without-write behavior, explicit write approval, and basic read/list operations.

## Security boundary

All requested paths are resolved against a configured workspace root and rejected if the resolved path escapes that root. This is a deliberately narrow baseline, not a complete sandbox. A production coding agent should additionally use process isolation, OS-level sandboxing, dependency controls, secret scanning, resource limits, audit logs, human approval for consequential changes, and repository-specific authorization.

## Production status

This quickstart is a learning and integration foundation. It is not production-ready evidence for autonomous coding or unrestricted code execution.
