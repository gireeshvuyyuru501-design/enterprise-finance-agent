from datetime import datetime

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session import Base


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    request: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    workflow: Mapped[str] = mapped_column(
        String(100),
        default="langgraph",
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="completed",
    )

    selected_agents: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    result: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )