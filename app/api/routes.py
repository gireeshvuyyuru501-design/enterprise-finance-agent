from fastapi import Depends, FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.agents.supervisor import SupervisorAgent
from app.database.models import AgentRun
from app.database.repository import (
    create_agent_run,
    get_agent_run,
    list_agent_runs,
)
from app.database.session import Base, engine, get_db
from app.workflows.finance_graph import run_finance_graph


Base.metadata.create_all(bind=engine)


api = FastAPI(
    title="Enterprise Finance Agent API",
    description=(
        "Multi-agent finance application using "
        "FastAPI, MCP, LangGraph and SQLAlchemy."
    ),
    version="2.0.0",
)


class AgentRequest(BaseModel):
    request: str = Field(
        min_length=3,
        max_length=500,
    )


class LangGraphRequest(BaseModel):
    request: str = Field(
        default="Create a complete finance report",
        min_length=3,
        max_length=500,
    )


class AgentRunResponse(BaseModel):
    id: int
    request: str
    workflow: str
    status: str
    selected_agents: list
    result: dict
    error_message: str | None
    created_at: str


def serialize_run(record: AgentRun) -> dict:
    return {
        "id": record.id,
        "request": record.request,
        "workflow": record.workflow,
        "status": record.status,
        "selected_agents": record.selected_agents,
        "result": record.result,
        "error_message": record.error_message,
        "created_at": record.created_at.isoformat(),
    }


@api.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "version": "2.0.0",
        "database": "connected",
    }


@api.post("/agent/run")
async def run_agent(payload: AgentRequest) -> dict:
    try:
        supervisor = SupervisorAgent()
        return await supervisor.run(payload.request)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc


@api.post("/langgraph/run")
def run_langgraph_agent(
    payload: LangGraphRequest,
    db: Session = Depends(get_db),
) -> dict:
    try:
        result = run_finance_graph(payload.request)

        record = create_agent_run(
            db=db,
            request=payload.request,
            result=result,
            selected_agents=result.get("plan", []),
        )

        return {
            "run_id": record.id,
            "status": record.status,
            "report": result,
        }

    except Exception as exc:
        create_agent_run(
            db=db,
            request=payload.request,
            result={},
            selected_agents=[],
            status="failed",
            error_message=str(exc),
        )

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc


@api.get("/runs")
def get_runs(
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
) -> list[dict]:
    records = list_agent_runs(
        db=db,
        limit=limit,
    )

    return [
        serialize_run(record)
        for record in records
    ]


@api.get("/runs/{run_id}")
def get_run_by_id(
    run_id: int,
    db: Session = Depends(get_db),
) -> dict:
    record = get_agent_run(
        db=db,
        run_id=run_id,
    )

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Agent run not found",
        )

    return serialize_run(record)