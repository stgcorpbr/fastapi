import os
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel as PydanticBaseModel


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DBBaseModel = declarative_base()

    DB_BASE = 'DB_00525580'
    URL_MYSQL: str = "mysql+aiomysql://userdb:SysDb123#ee@stgbd.cf"

    DB_URL: str = f"{URL_MYSQL}/{DB_BASE}"
    DB_URL_GERENCIAL: str = f"{URL_MYSQL}/gerencial"
    DB_URL_SISTEMAS: str = f"{URL_MYSQL}/sc_sistemas"

    JWT_SECRET: str = '6nyZ5uIN2vgrbBxT7pM-d-h97ws8oYzlHLuP4WiUASc'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """

    ALGORITHM: str = 'HS256'

    # 60 Minutos * 24 horas * 7 dias => 1 Semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 

    # APP_ENV = os.getenv('APP_ENV', 'development')
    # DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgress')
    # DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123mudar')
    # DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    # DATABASE_NAME = os.getenv('DATABASE_NAME', 'sc_sistemas')
    # TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'sc_sistemas_test')

    REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.getenv('REDIS_PORT', '6379')
    REDIS_DB = os.getenv('REDIS_DB', '0')

    class Config:
        case_sensitive = True
        arbitrary_types_allowed = True

settings: Settings = Settings()