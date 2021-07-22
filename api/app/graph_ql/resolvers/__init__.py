from .case import case, docketentry
from .query import query
from .mutations import mutation

resolvers = [query, mutation, case, docketentry]
