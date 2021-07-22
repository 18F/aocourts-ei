from datetime import datetime

from ariadne import ScalarType


def serialize_datetime(value: datetime) -> str:
    date = value
    if format:
        return date.strftime("%Y-%m-%d")
    else:
        return date.isoformat()


def parse_datetime_value(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


datetime_scalar = ScalarType(
    "Datetime",
    serializer=serialize_datetime,
    value_parser=parse_datetime_value
)
