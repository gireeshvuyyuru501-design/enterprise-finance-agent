from __future__ import annotations

from typing import Any

from fastmcp import Client

from app.agents.base import BaseAgent


class PortfolioAgent(BaseAgent):
    name = "Portfolio Agent"

    async def run(self, client: Client) -> dict[str, Any]:
        result = await client.call_tool("portfolio_summary", {})
        return {"agent": self.name, "result": result.data}


class BudgetAgent(BaseAgent):
    name = "Budget Agent"

    async def run(self, client: Client) -> dict[str, Any]:
        result = await client.call_tool("budget_summary", {})
        return {"agent": self.name, "result": result.data}


class ExpenseAgent(BaseAgent):
    name = "Expense Agent"

    async def run(self, client: Client) -> dict[str, Any]:
        result = await client.call_tool("expense_summary", {})
        return {"agent": self.name, "result": result.data}


class RiskAgent(BaseAgent):
    name = "Risk Agent"

    async def run(self, client: Client) -> dict[str, Any]:
        result = await client.call_tool("risk_summary", {})
        return {"agent": self.name, "result": result.data}
