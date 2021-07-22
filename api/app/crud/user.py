from typing import Optional, List, Any

from sqlalchemy.orm import Session

from app.schemas.user import UserInput
from app.models import User, Role
from app.core.security import verify_password, get_password_hash


class CrudUser:
    '''
    Create, read, update, and delete users
    '''
    def get(self, db: Session, id: Any) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_many(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(self, db: Session, user: UserInput) -> User:
        db_roles = db.query(Role).filter(Role.rolename.in_(r.rolename for r in user.roles)).all()

        db_user = User(
            email=user.email,
            hashed_password=get_password_hash(user.password),
            roles=db_roles
        )
        db.add(db_user)
        db.commit()

        return db_user

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active


user = CrudUser()
