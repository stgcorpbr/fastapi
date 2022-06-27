from pytz import timezone

from typing import Optional
from datetime import datetime, timedelta

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import user_model

from jose import jwt

from core.security import verificar_senha

from core.configs import settings
from fastapi.security import OAuth2PasswordBearer


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticar(cliente_id: int, senha: str, db: AsyncSession) -> Optional[user_model.AuthUser]:
    async with db as session:
        query = select(user_model.AuthUser).filter(user_model.AuthUser.is_active == 1, user_model.AuthUser.id == cliente_id)
        result = await session.execute(query)
        user: user_model.AuthUser = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not verificar_senha(senha, user.password):
            return None
        
        return user

def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rtf7519#section-4.1.3

    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_vida

    payload['type'] = tipo_token
    payload['exp'] = expira
    payload['iat'] = datetime.now(tz=sp)
    payload['sub'] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
    

def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io
    """
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
