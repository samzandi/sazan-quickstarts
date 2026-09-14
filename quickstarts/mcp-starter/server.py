from __future__ import annotations

from mcp.server import MCPServer

from tools import SAFE_TOOLS

mcp = MCPServer(
    "Sazan MCP Starter",
    instructions="Expose only explicitly allowlisted, narrow, non-destructive tools.",
)

# Security boundary: only functions declared in SAFE_TOOLS are exposed.
for tool in SAFE_TOOLS:
    mcp.tool()(tool)


@mcp.resource("sazan://about")
def about() -> str:
    """Describe this starter server."""
    return "Sazan MCP Starter exposes small, auditable, explicitly allowlisted tools."


if __name__ == "__main__":
    mcp.run(transport="streamable-http", json_response=True)
