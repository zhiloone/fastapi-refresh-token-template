from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from src.config import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
    """Ensure the database schema is created."""
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session():
    """Dependency to provide a session."""
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
