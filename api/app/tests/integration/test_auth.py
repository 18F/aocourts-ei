import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.core.config import settings


def test_get_access_token_valid_user(client: TestClient, db_session: Session, default_user) -> None:
    '''Correct credentials should return HTTP 200 and an access token'''
    login_data = {
        "username": settings.INITIAL_ADMIN_USER,
        "password": settings.INITIAL_ADMIN_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


@pytest.mark.parametrize('login_data', [
    {"username": settings.INITIAL_ADMIN_USER, "password": "Whoops"},
    {"username": 'bad@example.com', "password": settings.INITIAL_ADMIN_PASSWORD},
    {"username": 'bad@example.com', "password": 'whoops'},
])
def test_get_access_token_invalid_user(login_data, client: TestClient, db_session: Session, default_user) -> None:
    '''Incorrect credentials should return HTTP 400 and no token'''
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 400
    assert "access_token" not in tokens


@pytest.mark.parametrize('login_data', [
    {"username": '', "password": 'Whoops'},
    {"username": '', "password": ''},
    {"username": 'bad@example.com', "password": ''},
    {"username": None, "password": None},
])
def test_get_access_token_bad_input(login_data, client: TestClient, db_session: Session, default_user) -> None:
    '''Missing credentials should return HTTP 422'''
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 422
    assert "access_token" not in tokens
