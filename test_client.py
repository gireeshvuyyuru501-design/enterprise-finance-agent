from __future__ import annotations

import asyncio
import json
from pathlib import Path

from fastmcp import Client

SERVER_PATH = str(
    Path(__file__).resolve().parent / "app" / "mcp" / "server.py"
)


async def main() -> None:
    client = Client(SERVER_PATH)

    async with client:
        tools = await client.list_tools()
        print("Connected to MCP server.")
        print("Available tools:")

        for tool in tools:
            print(f"- {tool.name}")

        result = await client.call_tool("complete_finance_report", {})
        print("\nComplete report:")
        print(json.dumps(result.data, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
