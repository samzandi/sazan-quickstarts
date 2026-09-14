# Email Agent

A minimal, provider-neutral email quickstart focused on safe classification, draft-only replies, and explicit human approval.

## What it does
- reads only from a bounded local mock mailbox
- classifies routine, urgent, sensitive, and unsupported messages
- drafts replies without sending by default
- requires explicit approval before a send simulation
- escalates sensitive and unsupported messages

## Safety boundaries
This example does **not** connect to a real mailbox, store credentials, mutate inbox state, delete or forward messages, execute attachments, call external services, or send real email. Payment, account, legal, medical, security, and ambiguous requests are escalated.

## Run locally
```bash
cd quickstarts/email-agent
python app.py
python -m unittest discover -s tests -v
```

## Status
Educational quickstart only. It is not production-ready and has not been hardened for real customer data, authentication, privacy requirements, attachment scanning, audit logging, rate limiting, observability, or live mail providers.
