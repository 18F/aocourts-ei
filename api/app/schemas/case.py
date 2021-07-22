import datetime
from .docket_entry import DocketEntry, DocketEntryCreate
from typing import List, Literal, Union

from pydantic import BaseModel
from app.core.enums import CourtType


class CaseBase(BaseModel):
    '''
    Shared properties. All cases need these
    even when first creating them.
    '''
    title: str
    date_filed: datetime.date
    sealed: bool = False

    class Config:
        orm_mode = True


class CaseInput(CaseBase):
    '''
    Docket entries won't have things like IDs until
    they are in the DB.
    '''
    docket_entries: List[DocketEntryCreate] = []


class AppellateCaseInput(CaseInput):
    '''
    Appleate cases need a few extra things at creating time
    '''
    original_case_id: int
    reviewed: bool = False
    remanded: bool = False


# After cases are in the Database they will have properties
# like ID and the datetime created. These should be returned
# to the API caller.

class _Case(CaseBase):
    id: int
    created_at: datetime.datetime
    updated_on: datetime.datetime
    docket_entries: List[DocketEntry] = []
    type: CourtType


class DistrictCase(_Case):
    type: Literal[CourtType.district]


class BankruptcyCase(_Case):
    type: Literal[CourtType.bankruptcy]


class AppellateCase(_Case):
    type: Literal[CourtType.appellate]
    original_case_id: int
    reviewed: bool = False
    remanded: bool = False


Case = Union[DistrictCase, AppellateCase, BankruptcyCase]
