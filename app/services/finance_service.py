from __future__ import annotations

from collections import defaultdict
from typing import Any


def calculate_return(
    symbol: str,
    purchase_price: float,
    current_price: float,
    shares: float,
) -> dict[str, Any]:
    if purchase_price <= 0:
        raise ValueError("purchase_price must be greater than zero")
    if current_price < 0:
        raise ValueError("current_price cannot be negative")
    if shares < 0:
        raise ValueError("shares cannot be negative")

    invested = purchase_price * shares
    current_value = current_price * shares
    gain_loss = current_value - invested
    return_percent = (gain_loss / invested * 100) if invested else 0.0

    return {
        "symbol": symbol.upper(),
        "invested": round(invested, 2),
        "current_value": round(current_value, 2),
        "gain_loss": round(gain_loss, 2),
        "return_percent": round(return_percent, 2),
    }


def build_portfolio_summary(holdings: list[dict[str, Any]]) -> dict[str, Any]:
    positions = [
        calculate_return(
            symbol=str(item["symbol"]),
            purchase_price=float(item["purchase_price"]),
            current_price=float(item["current_price"]),
            shares=float(item["shares"]),
        )
        for item in holdings
    ]

    total_invested = sum(item["invested"] for item in positions)
    total_value = sum(item["current_value"] for item in positions)
    gain_loss = total_value - total_invested
    return_percent = (gain_loss / total_invested * 100) if total_invested else 0.0

    return {
        "positions": positions,
        "total_invested": round(total_invested, 2),
        "total_value": round(total_value, 2),
        "total_gain_loss": round(gain_loss, 2),
        "return_percent": round(return_percent, 2),
    }


def build_budget_summary(
    monthly_income: float,
    expenses: list[dict[str, Any]],
) -> dict[str, Any]:
    if monthly_income < 0:
        raise ValueError("monthly_income cannot be negative")

    total_expenses = sum(float(item["amount"]) for item in expenses)
    remaining = monthly_income - total_expenses
    savings_rate = (remaining / monthly_income * 100) if monthly_income else 0.0

    return {
        "monthly_income": round(monthly_income, 2),
        "total_expenses": round(total_expenses, 2),
        "remaining": round(remaining, 2),
        "savings_rate_percent": round(savings_rate, 2),
        "status": "within budget" if remaining >= 0 else "over budget",
    }


def build_expense_summary(expenses: list[dict[str, Any]]) -> dict[str, Any]:
    totals: dict[str, float] = defaultdict(float)

    for expense in expenses:
        category = str(expense.get("category") or "Other").title()
        totals[category] += float(expense["amount"])

    categories = sorted(
        [
            {"category": category, "amount": round(amount, 2)}
            for category, amount in totals.items()
        ],
        key=lambda item: item["amount"],
        reverse=True,
    )

    return {
        "categories": categories,
        "largest_category": categories[0] if categories else None,
    }


def build_risk_summary(portfolio: dict[str, Any]) -> dict[str, Any]:
    positions = portfolio.get("positions", [])
    if not positions:
        return {"risk_level": "unknown", "reasons": ["No portfolio positions found."]}

    total_value = portfolio["total_value"]
    weights = []

    for position in positions:
        weight = (
            position["current_value"] / total_value * 100
            if total_value
            else 0.0
        )
        weights.append(
            {
                "symbol": position["symbol"],
                "weight_percent": round(weight, 2),
            }
        )

    largest = max(weights, key=lambda item: item["weight_percent"])
    reasons = []

    if largest["weight_percent"] >= 50:
        risk_level = "high"
        reasons.append(
            f"{largest['symbol']} represents {largest['weight_percent']}% of portfolio value."
        )
    elif largest["weight_percent"] >= 35:
        risk_level = "moderate"
        reasons.append(
            f"{largest['symbol']} is the largest position at {largest['weight_percent']}%."
        )
    else:
        risk_level = "low"
        reasons.append("No single holding exceeds 35% of portfolio value.")

    return {
        "risk_level": risk_level,
        "position_weights": weights,
        "largest_position": largest,
        "reasons": reasons,
    }
