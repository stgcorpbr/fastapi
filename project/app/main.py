from distutils.log import debug
import os
from turtle import title
from celery import Celery
from fastapi import FastAPI
from fastapi import WebSocket
from fastapi.responses import HTMLResponse
from core.configs import settings
from api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache
from sqlalchemy.orm import Session

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

LOCAL_REDIS_URL = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"

@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', debug=True, reload=True)