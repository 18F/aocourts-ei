from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    '''
    App-wide configurations. Where values are not provided this will attempt
    to use evnironmental variables or look in an `.env` file in the main directory.
    '''
    API_V1_STR: str = "/api/v1"
    GRAPHQL_ENDPOINT: str = "/graphql"
    PROJECT_NAME: str = "AO Backend"
    SECRET_KEY: str = "123"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DATABASE_URL: str = "sqlite://"
    DATABASE_URL_TEST: str = "sqlite://"
    INITIAL_ADMIN_USER: str = "admin@example.com"
    INITIAL_ADMIN_PASSWORD: str = "secret"

    @validator("DATABASE_URL", pre=True)
    def fix_postgres_url(cls, v: str) -> str:
        '''Fixes DATABASE_URL from Cloud.gov so sqlalchemy will accept it'''
        if v.startswith("postgres://"):
            return v.replace("postgres://", "postgresql://", 1)
        return v

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
