from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agents.supervisor import SupervisorAgent
from app.workflows.finance_graph import run_finance_graph


api = FastAPI(
    title="Enterprise Finance Agent API",
    version="1.0.0",
)


class AgentRequest(BaseModel):
    request: str = Field(
        min_length=3,
        max_length=500,
    )


class LangGraphRequest(BaseModel):
    request: str = "Create a complete finance report"


@api.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}


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
def run_langgraph_agent(payload: LangGraphRequest) -> dict:
    try:
        return run_finance_graph(payload.request)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc