from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from app.crud import user, role
from app.core.config import settings
from app.schemas import UserInput, Role
from app.db import Base


def init_db(db: Session) -> None:
    '''This is a stub for inserting initial data that may be needed for the application,
    such as initial users. At the moment this is just a couple roles and
    an admin user with these roles assigned.

    Structural changes to the database should happen in migrations, not here.
    In fact, if if turns out data like roles is needed for the application, we
    may opt to put this in migrations as well.
    '''
    initial = user.get_by_email(db, email=settings.INITIAL_ADMIN_USER)
    if not initial:
        admin_role = Role.from_orm(role.get_by_name(db, rolename='admin'))
        clerk_role = Role.from_orm(role.get_by_name(db, rolename='clerk'))

        ''' How do you get secrets into Cloud.gov '''
        user_in = UserInput(
            email=settings.INITIAL_ADMIN_USER,
            password=settings.INITIAL_ADMIN_PASSWORD,
            roles=[admin_role, clerk_role]
        )

        initial = user.create(db, user=user_in)  # noqa: F841


def create_tables():
    '''Set up tables for the tests'''
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
