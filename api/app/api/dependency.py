from typing import Iterable

from pydantic import ValidationError
from fastapi import Depends, HTTPException, status
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app import models, schemas, crud
from app.core import security
from app.db import get_db

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(current_user: models.User = Depends(get_current_user)) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


class AllowRoles():
    def __init__(self, roles: Iterable[str]):
        self.autorized_roles = list(roles)

    def __call__(self, user: models.User = Depends(get_current_active_user)) -> models.User:
        if not any(role.rolename in self.autorized_roles for role in user.roles):
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return user
