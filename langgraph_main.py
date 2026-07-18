from __future__ import annotations

import json

from app.workflows.finance_graph import run_finance_graph


def main() -> None:
    print("=" * 60)
    print("ENTERPRISE FINANCE LANGGRAPH AGENT")
    print("=" * 60)

    request = input(
        "What should the finance agents do? "
    ).strip()

    if not request:
        request = "Create a complete finance report"

    result = run_finance_graph(request)

    print("\nFINAL LANGGRAPH RESULT")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()