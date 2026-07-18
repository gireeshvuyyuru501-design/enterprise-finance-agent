from __future__ import annotations

from typing import Any, TypedDict

from langgraph.graph import END, START, StateGraph

from app.services.data_service import load_finance_data
from app.services.finance_service import (
    build_budget_summary,
    build_expense_summary,
    build_portfolio_summary,
    build_risk_summary,
)


class FinanceState(TypedDict, total=False):
    request: str
    plan: list[str]
    finance_data: dict[str, Any]
    portfolio_result: dict[str, Any]
    budget_result: dict[str, Any]
    expense_result: dict[str, Any]
    risk_result: dict[str, Any]
    final_report: dict[str, Any]
    errors: list[str]


def supervisor_node(state: FinanceState) -> FinanceState:
    """Create the multi-agent execution plan."""

    return {
        "request": state.get(
            "request",
            "Create a complete finance report",
        ),
        "plan": [
            "Portfolio Agent",
            "Budget Agent",
            "Expense Agent",
            "Risk Agent",
            "Report Agent",
        ],
        "finance_data": load_finance_data(),
        "errors": [],
    }


def portfolio_node(state: FinanceState) -> FinanceState:
    """Run portfolio analysis."""

    try:
        holdings = state["finance_data"]["holdings"]

        return {
            "portfolio_result": build_portfolio_summary(holdings)
        }
    except Exception as exc:
        return {
            "portfolio_result": {},
            "errors": state.get("errors", [])
            + [f"Portfolio Agent error: {exc}"],
        }


def budget_node(state: FinanceState) -> FinanceState:
    """Run monthly budget analysis."""

    try:
        finance_data = state["finance_data"]

        result = build_budget_summary(
            finance_data["monthly_income"],
            finance_data["expenses"],
        )

        return {"budget_result": result}
    except Exception as exc:
        return {
            "budget_result": {},
            "errors": state.get("errors", [])
            + [f"Budget Agent error: {exc}"],
        }


def expense_node(state: FinanceState) -> FinanceState:
    """Analyze expenses by category."""

    try:
        expenses = state["finance_data"]["expenses"]

        return {
            "expense_result": build_expense_summary(expenses)
        }
    except Exception as exc:
        return {
            "expense_result": {},
            "errors": state.get("errors", [])
            + [f"Expense Agent error: {exc}"],
        }


def risk_node(state: FinanceState) -> FinanceState:
    """Calculate portfolio concentration risk."""

    try:
        portfolio = state.get("portfolio_result", {})

        return {
            "risk_result": build_risk_summary(portfolio)
        }
    except Exception as exc:
        return {
            "risk_result": {},
            "errors": state.get("errors", [])
            + [f"Risk Agent error: {exc}"],
        }


def report_node(state: FinanceState) -> FinanceState:
    """Combine specialist-agent results into one report."""

    portfolio = state.get("portfolio_result", {})
    budget = state.get("budget_result", {})
    expenses = state.get("expense_result", {})
    risk = state.get("risk_result", {})

    observations: list[str] = []

    if portfolio:
        observations.append(
            f"Portfolio return is "
            f"{portfolio.get('return_percent', 0):.2f}%."
        )

    if budget:
        observations.append(
            f"Savings rate is "
            f"{budget.get('savings_rate_percent', 0):.2f}%."
        )

    largest_expense = expenses.get("largest_category")

    if largest_expense:
        observations.append(
            f"Largest expense is "
            f"{largest_expense.get('category')} at "
            f"${largest_expense.get('amount', 0):.2f}."
        )

    if risk:
        observations.append(
            f"Portfolio concentration risk is "
            f"{risk.get('risk_level', 'unknown')}."
        )

    final_report = {
        "generated_by": "LangGraph Report Agent",
        "workflow": "Enterprise Finance Multi-Agent Graph",
        "request": state.get("request"),
        "plan": state.get("plan", []),
        "sections": {
            "Portfolio Agent": portfolio,
            "Budget Agent": budget,
            "Expense Agent": expenses,
            "Risk Agent": risk,
        },
        "observations": observations,
        "errors": state.get("errors", []),
        "disclaimer": (
            "Educational analysis only. This system does not "
            "provide personalized financial advice or execute trades."
        ),
    }

    return {"final_report": final_report}


def build_finance_graph():
    """Build and compile the finance-agent graph."""

    graph = StateGraph(FinanceState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("portfolio_agent", portfolio_node)
    graph.add_node("budget_agent", budget_node)
    graph.add_node("expense_agent", expense_node)
    graph.add_node("risk_agent", risk_node)
    graph.add_node("report_agent", report_node)

    graph.add_edge(START, "supervisor")
    graph.add_edge("supervisor", "portfolio_agent")
    graph.add_edge("portfolio_agent", "budget_agent")
    graph.add_edge("budget_agent", "expense_agent")
    graph.add_edge("expense_agent", "risk_agent")
    graph.add_edge("risk_agent", "report_agent")
    graph.add_edge("report_agent", END)

    return graph.compile()


finance_graph = build_finance_graph()


def run_finance_graph(
    request: str = "Create a complete finance report",
) -> dict[str, Any]:
    """Run the compiled LangGraph workflow."""

    result = finance_graph.invoke({"request": request})

    return result["final_report"]