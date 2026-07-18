from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Add the project root to Python's module search path.
# This is required because FastMCP launches this file as a subprocess.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fastmcp import FastMCP

from app.services.data_service import load_finance_data
from app.services.finance_service import (
    build_budget_summary,
    build_expense_summary,
    build_portfolio_summary,
    build_risk_summary,
)

mcp = FastMCP(
    "Enterprise Finance MCP Server",
    instructions=(
        "Use these tools for educational financial analysis. "
        "Do not execute trades or provide personalized financial advice."
    ),
)


@mcp.tool
def portfolio_summary() -> dict[str, Any]:
    """Return calculated performance for all portfolio holdings."""
    data = load_finance_data()
    return build_portfolio_summary(data["holdings"])


@mcp.tool
def budget_summary() -> dict[str, Any]:
    """Return income, expenses, remaining cash, and savings rate."""
    data = load_finance_data()

    return build_budget_summary(
        data["monthly_income"],
        data["expenses"],
    )


@mcp.tool
def expense_summary() -> dict[str, Any]:
    """Group expenses and identify the largest expense category."""
    data = load_finance_data()
    return build_expense_summary(data["expenses"])


@mcp.tool
def risk_summary() -> dict[str, Any]:
    """Calculate basic portfolio concentration risk."""
    data = load_finance_data()
    portfolio = build_portfolio_summary(data["holdings"])

    return build_risk_summary(portfolio)


@mcp.tool
def complete_finance_report() -> dict[str, Any]:
    """Generate a complete portfolio, budget, expense, and risk report."""
    data = load_finance_data()

    portfolio = build_portfolio_summary(data["holdings"])

    budget = build_budget_summary(
        data["monthly_income"],
        data["expenses"],
    )

    expenses = build_expense_summary(data["expenses"])
    risk = build_risk_summary(portfolio)

    observations = [
        f"Portfolio return: {portfolio['return_percent']:.2f}%.",
        f"Monthly savings rate: {budget['savings_rate_percent']:.2f}%.",
        f"Portfolio concentration risk: {risk['risk_level']}.",
    ]

    largest = expenses.get("largest_category")

    if largest:
        observations.append(
            f"Largest expense category: "
            f"{largest['category']} at "
            f"${largest['amount']:.2f}."
        )

    return {
        "portfolio": portfolio,
        "budget": budget,
        "expenses": expenses,
        "risk": risk,
        "observations": observations,
        "disclaimer": (
            "Educational analysis only. This application does not "
            "provide personalized financial advice or execute trades."
        ),
    }


if __name__ == "__main__":
    mcp.run()