import datetime

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import DateTime


class TimeStamps(object):
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
