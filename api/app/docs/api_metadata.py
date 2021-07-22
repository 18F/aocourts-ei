'''
tags_metadata is used when serving the swagger API documentation.
Each dictionary corresponds to a tag used in the API. The descriptions
will apear in the docs.
'''
tags_metadata = [
    {
        "name": "login",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "cases",
        "description": "Manage cases and their metadata",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://github.com/ao-api",
        },
    },
    {
        "name": "GraphQL",
        "description": "- **GET:** the GraphQL sandbox  \n- **POST:** handle graphQL queries."
    }
]
