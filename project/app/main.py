from distutils.log import debug
from turtle import title
from celery import Celery
from fastapi import FastAPI
from fastapi import WebSocket
from fastapi.responses import HTMLResponse
from core.configs import settings
from api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
app: FastAPI = FastAPI(title='Cliente API - FastApi SQL Model', debug=True)


# Your CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


celery_ = Celery(
    __name__,
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
)

celery_.conf.imports = [
    'core.tasks'
]

@app.on_event("startup")
async def startup():
    redis =  aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', debug=True, reload=True)