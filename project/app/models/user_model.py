from sqlmodel import Field, SQLModel
# from sqlalchemy.orm import relationship
from sqlalchemy import CHAR, DECIMAL, Date, Integer, String, Column, Boolean, DateTime, Text, TIMESTAMP, INT
from core.configs import settings
# from sqlalchemy import text

class AuthUser(settings.DBBaseModel):
    __tablename__ = 'auth_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Boolean)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean)
    is_active = Column(Boolean)
    date_joined = Column(DateTime, nullable=False)

