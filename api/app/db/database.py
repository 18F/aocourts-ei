from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

uri = settings.DATABASE_URL

engine = create_engine(uri)
# Note: use "check_same_thread" for SQLite. ie:
# settings.DATABASE_URL, connect_args={"check_same_thread": False}, echo=True

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore
