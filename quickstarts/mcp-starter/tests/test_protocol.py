from __future__ import annotations

import unittest

from mcp import Client

from server import mcp


class MCPProtocolTests(unittest.IsolatedAsyncioTestCase):
    async def test_only_allowlisted_tools_are_exposed(self) -> None:
        async with Client(mcp, raise_exceptions=True) as client:
            result = await client.list_tools()
            self.assertEqual({tool.name for tool in result.tools}, {"add", "health"})

    async def test_add_through_mcp_protocol(self) -> None:
        async with Client(mcp, raise_exceptions=True) as client:
            result = await client.call_tool("add", {"a": 20, "b": 22})
            self.assertEqual(result.structured_content, {"result": 42})


if __name__ == "__main__":
    unittest.main()
