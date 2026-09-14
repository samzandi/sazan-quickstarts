from __future__ import annotations

from mcp.server import MCPServer

from tools import add, health

mcp = MCPServer("Sazan MCP Starter")

mcp.tool()(add)
mcp.tool()(health)


@mcp.resource("sazan://about")
def about() -> str:
    """Describe this starter server."""
    return "Sazan MCP Starter exposes small, auditable example tools and resources."


if __name__ == "__main__":
    mcp.run(transport="streamable-http", json_response=True)
