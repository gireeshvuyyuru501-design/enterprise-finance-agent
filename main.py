from __future__ import annotations

import asyncio
import json

from app.agents.supervisor import SupervisorAgent


async def main() -> None:
    supervisor = SupervisorAgent()

    print("Enterprise Finance Agentic AI")
    print("Type exit to stop.")

    while True:
        request = input("\nWhat should the finance agents do? ").strip()

        if request.lower() in {"exit", "quit"}:
            break

        if not request:
            continue

        try:
            result = await supervisor.run(request)
            print("\nFINAL RESULT")
            print(json.dumps(result, indent=2))
        except Exception as exc:
            print(f"\nERROR: {exc}")


if __name__ == "__main__":
    asyncio.run(main())
