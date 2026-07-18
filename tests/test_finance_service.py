from app.services.finance_service import (
    build_budget_summary,
    build_portfolio_summary,
    calculate_return,
)


def test_calculate_return() -> None:
    result = calculate_return("ABC", 100, 120, 2)
    assert result["gain_loss"] == 40
    assert result["return_percent"] == 20


def test_budget_summary() -> None:
    result = build_budget_summary(
        5000,
        [{"name": "Rent", "category": "Housing", "amount": 1500}],
    )
    assert result["remaining"] == 3500
    assert result["status"] == "within budget"


def test_portfolio_summary() -> None:
    result = build_portfolio_summary(
        [{"symbol": "ABC", "purchase_price": 10, "current_price": 12, "shares": 5}]
    )
    assert result["total_gain_loss"] == 10
