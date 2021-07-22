import datetime

from pydantic import BaseModel


# Shared properties
class DocketEntryBase(BaseModel):
    text: str
    sequence_no: int
    date_filed: datetime.date
    sealed: bool = False
    entry_type: str

    class Config:
        orm_mode = True


class DocketEntryCreate(DocketEntryBase):
    pass


# Properties to return to client
class DocketEntry(DocketEntryBase):
    id: int
    case_id: str
    created_at: datetime.datetime
    updated_on: datetime.datetime
