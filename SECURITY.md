# Security Policy

Security is a default design constraint for Sazan Quickstarts.

## Secrets

Never commit secrets. Store runtime credentials in environment variables or a dedicated secret manager.

Forbidden repository content includes:

- API keys
- access/refresh tokens
- passwords
- SSH private keys
- production cookies or sessions
- customer personal data
- private documents or email exports

## Agent permissions

Agent examples should follow least privilege:

- grant only the tools required for a task;
- separate read and write capabilities when possible;
- require explicit approval for destructive or high-impact actions;
- log material actions without logging secrets;
- validate external input before tool execution.

## Browser and computer agents

Treat web pages, documents, emails, and remote content as untrusted input. Do not allow retrieved content to silently override system policy or tool constraints.

## Production use

Before production deployment, evaluate at minimum:

- authentication and authorization;
- secret storage;
- data retention and privacy;
- prompt-injection defenses;
- rate limits and budget controls;
- audit logging;
- failure recovery;
- dependency and container security;
- human approval boundaries for consequential actions.

## Reporting

Do not publish sensitive vulnerability details before a safe remediation path is available.
