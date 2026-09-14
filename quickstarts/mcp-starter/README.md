# Sazan MCP Starter

Minimal Model Context Protocol server using the current MCP Python SDK v2 line.

## Features

- one calculator-style tool: `add`
- one health tool: `health`
- one static resource: `sazan://about`
- Streamable HTTP transport for deployment-style local testing

## Install

```bash
cd quickstarts/mcp-starter
python -m pip install -r requirements.txt
```

## Run

```bash
python server.py
```

Or use the official MCP CLI / Inspector:

```bash
mcp dev server.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Security note

Keep MCP tools narrowly scoped. Do not expose shell execution, filesystem mutation, credentials, destructive operations, or privileged network access without explicit authorization, validation, logging, and sandboxing.

## Production status

This is a starter and test fixture, not a production-ready MCP service. Production use still requires authentication, authorization, rate limits, observability, deployment hardening, and task-specific security review.
