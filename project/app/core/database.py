from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings
# from typing import Callable
# from sqlalchemy.orm import Session
# from contextlib import contextmanager, AbstractContextManager

# class Database:
#     def __init__(self, db_url:str) -> None:
#        self._engine: AsyncEngine = create_async_engine(db_url)
#        self._Session: AsyncSession = sessionmaker(
#             autocommit=False,
#             autoflush=False,
#             expire_on_commit=False,
#             class_=AsyncSession,
#             bind=self._engine
#         )

#     @contextmanager
#     def session(self) -> Callable[..., AbstractContextManager[Session]]:
#         session: Session = self._session_factory()
#         try:
#             yield session
#         except Exception:
#             logger.exception("Session rollback because of exception")
#             session.rollback()
#             raise
#         finally:
#             session.close()

engine: AsyncEngine = create_async_engine(settings.DB_URL)
engine_gerencial: AsyncEngine = create_async_engine(settings.DB_URL_GERENCIAL)
engine_sistemas: AsyncEngine = create_async_engine(settings.DB_URL_SISTEMAS)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

SessionGerencial: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine_gerencial
)

SessionSistemas: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine_sistemas
)