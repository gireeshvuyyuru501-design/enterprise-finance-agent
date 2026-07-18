from __future__ import annotations

from typing import Any


class ReportAgent:
    name = "Report Agent"

    def build(self, outputs: list[dict[str, Any]]) -> dict[str, Any]:
        sections = {
            output["agent"]: output["result"]
            for output in outputs
        }

        observations: list[str] = []

        portfolio = sections.get("Portfolio Agent")
        if portfolio:
            observations.append(
                f"Portfolio return is {portfolio['return_percent']:.2f}%."
            )

        budget = sections.get("Budget Agent")
        if budget:
            observations.append(
                f"Savings rate is {budget['savings_rate_percent']:.2f}%."
            )

        expenses = sections.get("Expense Agent")
        if expenses and expenses.get("largest_category"):
            largest = expenses["largest_category"]
            observations.append(
                f"Largest expense is {largest['category']} at ${largest['amount']:.2f}."
            )

        risk = sections.get("Risk Agent")
        if risk:
            observations.append(
                f"Portfolio concentration risk is {risk['risk_level']}."
            )

        return {
            "generated_by": self.name,
            "sections": sections,
            "observations": observations,
            "disclaimer": (
                "Educational analysis only. This system does not provide "
                "personalized investment advice or execute trades."
            ),
        }
