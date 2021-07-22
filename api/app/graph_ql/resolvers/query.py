from typing import Any, Optional
from ariadne import QueryType
from ariadne.types import GraphQLResolveInfo
from pydantic import parse_obj_as
from app.crud import case
from app.schemas import Case
query = QueryType()


@query.field("case")
def resolve_case(obj: Any, info: GraphQLResolveInfo, id) -> Optional[Case]:
    session = info.context['request'].state.db
    case_data = case.get(session, id)
    if case_data:
        return parse_obj_as(Case, case_data)
