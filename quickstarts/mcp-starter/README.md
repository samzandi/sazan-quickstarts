# Sazan MCP Starter

Minimal Model Context Protocol server using the current MCP Python SDK v2 line.

## Features

- explicit `SAFE_TOOLS` allowlist; functions are not exposed automatically
- one calculator-style tool: `add`
- one health tool: `health`
- one static resource: `sazan://about`
- in-process MCP client example for protocol-level testing without a port
- Streamable HTTP transport for deployment-style local testing
- GitHub Actions test matrix on Python 3.11, 3.12, and 3.13

## Install

```bash
cd quickstarts/mcp-starter
python -m pip install -r requirements.txt
```

## Run the in-process demo

```bash
python client.py
```

This connects a real MCP `Client` directly to the server object and exercises the protocol without a subprocess or network port.

## Run over Streamable HTTP

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

The protocol tests verify that only the allowlisted tools are visible and that `add` works through the MCP client/server layer.

## Security boundary

Keep the `SAFE_TOOLS` registry narrow. Adding a Python function does not expose it unless it is explicitly registered. Do not expose shell execution, filesystem mutation, credentials, destructive operations, or privileged network access without explicit authorization, validation, logging, and sandboxing.

## Production status

This is a starter and test fixture, not a production-ready MCP service. Production use still requires authentication, authorization, rate limits, observability, deployment hardening, and task-specific security review.
