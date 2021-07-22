from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from app.db.database import Base
from app.core.enums import CourtType
from .mixins import TimeStamps


class Case(TimeStamps, Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date_filed = Column(DateTime)
    sealed = Column(Boolean, default=False)
    docket_entries = relationship("DocketEntry", cascade="all, delete")
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'case'
    }


class DistrictCase(Case):
    __mapper_args__ = {
        'polymorphic_identity': CourtType.district
    }


class AppellateCase(Case):
    original_case_id = Column(Integer)
    reviewed = Column(Boolean, default=False)
    remanded = Column(Boolean, default=False)
    __mapper_args__ = {
        'polymorphic_identity': CourtType.appellate
    }
