from app.database import models
from app.database.session import Base, engine


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)
    print("DATABASE INITIALIZED SUCCESSFULLY")


if __name__ == "__main__":
    initialize_database()