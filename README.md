# Enterprise Finance Agentic AI with MCP

A modular beginner-friendly Agentic AI project built with Python, FastMCP, FastAPI, and multiple specialized agents.

## Agents

- Supervisor Agent
- Portfolio Agent
- Budget Agent
- Expense Agent
- Risk Agent
- Report Agent

## MCP tools

- portfolio_summary
- budget_summary
- expense_summary
- risk_summary
- complete_finance_report

## Windows setup

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Test MCP server

```powershell
python test_client.py
```

## Run multi-agent console

```powershell
python main.py
```

Example:

```text
Create a complete finance report
Analyze my portfolio risk
Show budget and expense summary
```

## Run FastAPI

```powershell
uvicorn app.api.routes:api --reload
```

Open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## Run tests

```powershell
pytest -q
```

## Safety

Educational use only. This project does not provide personalized financial advice and does not execute trades.
