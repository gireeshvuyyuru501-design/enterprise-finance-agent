# 💰 # Enterprise Multi-Agent Finance AI with MCP

> A production-style **Multi-Agent Finance AI Platform** built using **Python, FastAPI, LangGraph, FastMCP, SQLAlchemy, Docker, and MCP**.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-AgenticAI-orange)
![MCP](https://img.shields.io/badge/MCP-FastMCP-purple)
![License](https://img.shields.io/badge/License-MIT-success)

---

# 📌 Overview

Enterprise Finance Agent is a modular Agentic AI application that coordinates multiple specialized financial agents to analyze investment portfolios, budgets, expenses, and financial risks.

The project demonstrates modern enterprise AI architecture using:

- Multi-Agent AI
- MCP (Model Context Protocol)
- LangGraph orchestration
- FastAPI REST APIs
- Docker deployment
- SQLAlchemy persistence
- Swagger API documentation

---

# 🚀 Features

- Multi-Agent Finance Assistant
- FastAPI REST APIs
- Docker & Docker Compose
- MCP Integration
- LangGraph Workflow
- SQLAlchemy Database
- Swagger/OpenAPI
- Modular Enterprise Architecture
- Execution History
- Portfolio Analysis
- Risk Assessment
- Budget Analysis
- Expense Tracking
- AI Report Generation

---

# 🤖 AI Agents

| Agent | Responsibility |
|---------|----------------|
| Supervisor Agent | Coordinates all AI agents |
| Portfolio Agent | Portfolio analysis |
| Budget Agent | Budget recommendations |
| Expense Agent | Expense analytics |
| Risk Agent | Risk scoring |
| Report Agent | Final AI report generation |

---

# 🔌 MCP Tools

- portfolio_summary
- budget_summary
- expense_summary
- risk_summary
- complete_finance_report

---

# 🏗 Project Architecture

```text
                    User
                      │
                      ▼
               FastAPI REST API
                      │
                      ▼
             Supervisor Agent
                      │
 ┌──────────┬──────────┬──────────┬──────────┐
 │          │          │          │          │
 ▼          ▼          ▼          ▼          ▼
Portfolio  Budget   Expense     Risk     Report
 Agent      Agent     Agent      Agent     Agent
 │
 ▼
MCP Tools
 │
 ▼
SQLAlchemy Database
 │
 ▼
SQLite / PostgreSQL
```

---

# 🔄 Agent Workflow

```text
User Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Supervisor Agent
      │
      ▼
Intent Detection
      │
      ▼
Agent Selection
      │
      ▼
Parallel Agent Execution
      │
      ▼
Result Aggregation
      │
      ▼
AI Finance Report
      │
      ▼
REST API Response
```

---

# 📂 Project Structure

```text
enterprise_finance_agent
│
├── app
│   ├── agents
│   ├── api
│   ├── database
│   ├── mcp
│   ├── services
│   └── workflows
│
├── tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── main.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/gireeshvuyyuru501-design/enterprise-finance-agent.git

cd enterprise-finance-agent
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Packages

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

---

# ▶ Run MCP Server

```bash
python test_client.py
```

---

# ▶ Run Multi-Agent Console

```bash
python main.py
```

Example prompts

```
Create a complete finance report

Analyze my investment portfolio

Show budget summary

Analyze financial risk

Generate expense report
```

---

# ▶ Run FastAPI

```bash
uvicorn app.api.routes:api --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

Health

```
http://127.0.0.1:8000/health
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# 🧪 Testing

```bash
pytest -q
```

---

# 🛠 Technology Stack

### AI

- LangGraph
- MCP
- FastMCP

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- SQLite
- PostgreSQL Ready

### DevOps

- Docker
- Docker Compose
- Git

---

# 📈 Future Improvements

- LangSmith Tracing
- Authentication
- PostgreSQL
- Redis
- Celery
- Kubernetes
- CI/CD
- AWS Deployment
- Azure Deployment
- Vector Database
- LLM Integration
- RAG Pipeline

---

# 📷 API Preview

Swagger UI

```
GET    /health

POST   /agent/run

POST   /langgraph/run

GET    /runs

GET    /runs/{run_id}
```

---

# ⚠ Disclaimer

This project is intended for educational and portfolio purposes.

It does **not** provide financial, legal, or investment advice and does not execute real trades.

---

# 👨‍💻 Author

**Girish V**

AI/ML Engineer • Generative AI Engineer • Python Developer

GitHub

https://github.com/gireeshvuyyuru501-design

LinkedIn

https://www.linkedin.com/in/girish-genai-engineer
