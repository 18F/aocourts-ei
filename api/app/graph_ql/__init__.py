'''This package is responsible for defining GraphQL types, schema, and also provides 
fastAPI routes for including with a fastAPI app

schema/     .graphql files defining the schema for the app. If there is more than file 
            they will be merged into a single schema. 
            [see also: https://ariadne.readthedocs.io/en/0.3.0/modularization.html]

routes.py   creates GraphQL app and adds routes for:
            GET route for the graphQL playground
            POST route for queries
            These get plugged into the main fastAPI app

schema.py   setup for Ariadne service

resolvers/  resolver functions for the graphQL types. In general, business logic
            should NOT go here. 

'''
from .schema import schema
