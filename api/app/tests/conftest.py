from typing import Generator, Any
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.db import Base, get_db
from sqlalchemy.orm import sessionmaker
from app.schemas import UserInput
from app.crud import user


engine = create_engine(settings.DATABASE_URL_TEST)
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True, scope="package")
def api_app() -> Generator[FastAPI, Any, None]:
    '''Set up tables for the tests'''
    Base.metadata.create_all(engine)
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(api_app: FastAPI) -> Generator[Session, Any, None]:
    '''Create a fresh session inside a transacation and roll it back after the test'''
    connection = engine.connect()
    transaction = connection.begin()
    session = TestSession(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(api_app: FastAPI, db_session: Session) -> Generator[TestClient, Any, None]:
    '''Uses FastAPIs dependency injection to replace the DB dependency everywhere'''

    def get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture()
def default_user(db_session: Session):
    test_user = UserInput(
        email=settings.INITIAL_ADMIN_USER,
        password=settings.INITIAL_ADMIN_PASSWORD,
        roles=[]
    )
    return user.create(db_session, test_user)
