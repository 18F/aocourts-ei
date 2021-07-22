# type: ignore
"""

add_roles

Revision ID: 7426da0d030a
Revises: 179a279f5647
Create Date: 2021-07-20 13:51:53.825585

"""
from alembic import op
from sqlalchemy import String
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '7426da0d030a'
down_revision = '179a279f5647'
branch_labels = None
depends_on = None


def upgrade():
    roles_table = table(
        'roles',
        column('rolename', String),
    )

    op.bulk_insert(
        roles_table,
        [
            {'rolename': 'admin'},
            {'rolename': 'clerk'},
            {'rolename': 'judge'},
        ]
    )


def downgrade():
    op.execute("delete from roles")
