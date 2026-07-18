from app.workflows.finance_graph import run_finance_graph


def test_complete_finance_graph():
    result = run_finance_graph(
        "Create a complete finance report"
    )

    assert result["generated_by"] == "LangGraph Report Agent"
    assert "Portfolio Agent" in result["sections"]
    assert "Budget Agent" in result["sections"]
    assert "Expense Agent" in result["sections"]
    assert "Risk Agent" in result["sections"]
    assert result["errors"] == []