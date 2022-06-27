import os
from typing import Optional

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@router.get('/home/{id}/teste/{name}')
async def index(id: int, name: str, amostra: Optional[str] = None):
    return {
        'data': {
            'id': id,
            'amostra' : amostra,
            'name': 'Fersoftware',
            'sobrenome': name
        }
    }
