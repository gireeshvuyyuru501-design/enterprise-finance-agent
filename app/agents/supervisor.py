from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

from fastmcp import Client

from app.agents.report_agent import ReportAgent
from app.agents.specialists import (
    BudgetAgent,
    ExpenseAgent,
    PortfolioAgent,
    RiskAgent,
)

SERVER_PATH = str(Path(__file__).resolve().parents[1] / "mcp" / "server.py")


class SupervisorAgent:
    def __init__(self) -> None:
        self.portfolio_agent = PortfolioAgent()
        self.budget_agent = BudgetAgent()
        self.expense_agent = ExpenseAgent()
        self.risk_agent = RiskAgent()
        self.report_agent = ReportAgent()

    def create_plan(self, request: str) -> list[Any]:
        text = request.lower()
        agents: list[Any] = []

        if "portfolio" in text or "investment" in text:
            agents.append(self.portfolio_agent)

        if "budget" in text or "saving" in text or "income" in text:
            agents.append(self.budget_agent)

        if "expense" in text or "spending" in text:
            agents.append(self.expense_agent)

        if "risk" in text or "concentration" in text:
            agents.append(self.risk_agent)

        if any(word in text for word in ("complete", "full", "report", "everything")):
            agents = [
                self.portfolio_agent,
                self.budget_agent,
                self.expense_agent,
                self.risk_agent,
            ]

        if not agents:
            agents = [
                self.portfolio_agent,
                self.budget_agent,
                self.expense_agent,
                self.risk_agent,
            ]

        return agents

    async def run(self, request: str) -> dict[str, Any]:
        agents = self.create_plan(request)
        client = Client(SERVER_PATH)

        async with client:
            outputs = await asyncio.gather(
                *(agent.run(client) for agent in agents)
            )

        return {
            "request": request,
            "plan": [agent.name for agent in agents],
            "report": self.report_agent.build(outputs),
        }
