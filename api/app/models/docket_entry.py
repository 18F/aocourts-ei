from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

from app.db.database import Base
from .mixins import TimeStamps


class DocketEntry(TimeStamps, Base):
    __tablename__ = "docket_entries"
    id = Column(Integer, nullable=False, primary_key=True)
    case_id = Column(Integer, ForeignKey('cases.id'), nullable=False)
    sequence_no = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    date_filed = Column(DateTime)
    entry_type = Column(String, nullable=False)
    sealed = Column(Boolean, default=False)
