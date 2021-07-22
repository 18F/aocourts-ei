from ariadne import MutationType
from pydantic import parse_obj_as
from app.crud import case
from app.schemas import Case

mutation = MutationType()


@mutation.field("sealCase")
def resolve_seal_case(obj, info, caseId, sealed):
    session = info.context['request'].state.db
    modified_case = case.set_sealed(session, caseId, sealed)
    return parse_obj_as(Case, modified_case)
