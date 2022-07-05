import os

from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
app: FastAPI = FastAPI(title='Cliente API - FastApi SQL Model', debug=True)

origins = [
    "https://www.stganalytics.com.br",
    "https://stganalytics.com.br",
    "http://stganalytics.com.br",    
    "http://stgapi.cf",
    "https://stgapi.cf",
    "https://stgapi.cf:8000",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8002",
    "http://localhost:9000",
]

# Your CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

LOCAL_REDIS_URL = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"

@app.on_event("startup")
async def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, AsyncSession, Session]
    )


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=9000, log_level='info', debug=True, reload=True)