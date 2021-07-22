import os

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers
)
from .resolvers import resolvers
from .scalars import datetime_scalar


dirname = os.path.dirname(__file__)
schema_dir = os.path.join(dirname, 'schemas/')
type_defs = load_schema_from_path(schema_dir)

schema = make_executable_schema(type_defs, *resolvers, datetime_scalar, snake_case_fallback_resolvers)
