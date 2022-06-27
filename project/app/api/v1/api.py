from fastapi import APIRouter

from api.v1.endpoints import home

api_router = APIRouter()
api_router.include_router(home.router, prefix='/clientes', tags=['clientes'])
