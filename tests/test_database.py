from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.repository import (
    create_agent_run,
    get_agent_run,
    list_agent_runs,
)
from app.database.session import Base


def create_test_session():
    engine = create_engine(
        "sqlite://",
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )

    Base.metadata.create_all(bind=engine)

    session_factory = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    return session_factory()


def test_create_and_read_agent_run():
    db = create_test_session()

    record = create_agent_run(
        db=db,
        request="Analyze expenses",
        result={"status": "complete"},
        selected_agents=["Expense Agent"],
    )

    stored = get_agent_run(
        db=db,
        run_id=record.id,
    )

    assert stored is not None
    assert stored.request == "Analyze expenses"
    assert stored.status == "completed"


def test_list_agent_runs():
    db = create_test_session()

    create_agent_run(
        db=db,
        request="Create report",
        result={"status": "complete"},
        selected_agents=["Report Agent"],
    )

    records = list_agent_runs(db)

    assert len(records) == 1