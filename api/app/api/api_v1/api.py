from fastapi import APIRouter

from app.api.api_v1.endpoints import cases, login

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(cases.router, prefix="/cases", tags=["cases"])
