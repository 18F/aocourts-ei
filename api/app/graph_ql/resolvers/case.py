from typing import List

from ariadne import ObjectType, InterfaceType
from ariadne.types import GraphQLResolveInfo
from app.schemas import DocketEntry, Case, DistrictCase, AppellateCase

case = InterfaceType("Case")
docketentry = ObjectType("DocketEntry")
docketentry.set_alias("sequenceNumber", "sequence_no")


@case.type_resolver
def case_result_type(obj, *_):
    if isinstance(obj, DistrictCase):
        return "DistrictCase"
    if isinstance(obj, AppellateCase):
        return "AppellateCase"


@case.field("docketEntries")
def resolve_docket_entries(obj: Case, info: GraphQLResolveInfo) -> List[DocketEntry]:
    # at the moment the crud query grabs the whole docket, so this is convenient
    # this will probably change
    return obj.docket_entries
