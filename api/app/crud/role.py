from typing import Optional, Any

from sqlalchemy.orm import Session

from app.schemas import RoleCreate
from app.models import Role


class CrudRole:
    '''
    Create, read, update, and delete roles
    '''
    def get(self, db: Session, id: Any) -> Optional[Role]:
        return db.query(Role).filter(Role.id == id).first()

    def get_by_name(self, db: Session, rolename: Any) -> Optional[Role]:
        return db.query(Role).filter(Role.rolename == rolename).first()

    def create(self, db: Session, role: RoleCreate) -> Role:
        db_role = Role(**role.dict())
        db.add(db_role)
        db.commit()
        return db_role


role = CrudRole()
