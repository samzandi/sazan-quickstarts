from __future__ import annotations

import asyncio

from mcp import Client

from server import mcp


async def main() -> None:
    # In-process client: real MCP protocol behavior without opening a network port.
    async with Client(mcp, raise_exceptions=True) as client:
        tools = await client.list_tools()
        print("Tools:", [tool.name for tool in tools.tools])

        result = await client.call_tool("add", {"a": 2, "b": 3})
        print("2 + 3 =", result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())
