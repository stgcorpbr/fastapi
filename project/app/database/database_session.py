# database_session.py
# import logging
# import os
# from typing import Callable, Optional

# import sqlalchemy
from sqlalchemy.orm import Session

# from app.database.modelbase import Base

# __factory: Optional[Callable[[], Session]] = None
# log = logging.getLogger("uvicorn")


def get_db() -> Session:
    db = create_session()
    try:
        yield db
    finally:
        db.close()


# def global_init(db) -> None:
#     global __factory

#     if __factory:
#         return

#     GERENCIAL_DB_URL = str(f"mysql+pymysql://userdb:SysDb123#ee@stgbd.cf/gerencial")
#     DB_URL = str(f"mysql+pymysql://userdb:SysDb123#ee@stgbd.cf/sc_sistemas")
#     SYSTEMAS_DB_URL = str(f"mysql+pymysql://userdb:SysDb123#ee@stgbd.cf/DB_{db}")

#     conn_str = str(f"mysql+pymysql://userdb:SysDb123#ee@stgbd.cf/DB_{db}")
#     log.info(f"Connecting to the database...{db}")
#     engine = sqlalchemy.create_engine(conn_str, echo=False)
#     __factory = sqlalchemy.orm.sessionmaker(bind=engine)

#     from app.models.register import Register

#     Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method")

    session: Session = __factory()
    session.expire_on_commit = False

    return session