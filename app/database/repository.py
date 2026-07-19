from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import AgentRun


def create_agent_run(
    db: Session,
    request: str,
    result: dict,
    selected_agents: list[str],
    status: str = "completed",
    error_message: str | None = None,
) -> AgentRun:
    record = AgentRun(
        request=request,
        workflow="langgraph",
        status=status,
        selected_agents=selected_agents,
        result=result,
        error_message=error_message,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def list_agent_runs(
    db: Session,
    limit: int = 20,
) -> list[AgentRun]:
    statement = (
        select(AgentRun)
        .order_by(AgentRun.created_at.desc())
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def get_agent_run(
    db: Session,
    run_id: int,
) -> AgentRun | None:
    return db.get(AgentRun, run_id)