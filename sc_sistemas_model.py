# coding: utf-8
from sqlalchemy import Column, DECIMAL, ForeignKey, Index, String
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(150), nullable=False, unique=True)


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DATETIME(fsp=6))
    is_superuser = Column(TINYINT(1), nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(TINYINT(1), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    date_joined = Column(DATETIME(fsp=6), nullable=False)


class ClientesFile(Base):
    __tablename__ = 'clientes_file'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(50), nullable=False)
    dt_criacao = Column(DATETIME(fsp=6))


class DjangoCeleryBeatClockedschedule(Base):
    __tablename__ = 'django_celery_beat_clockedschedule'

    id = Column(INTEGER(11), primary_key=True)
    clocked_time = Column(DATETIME(fsp=6), nullable=False)


class DjangoCeleryBeatCrontabschedule(Base):
    __tablename__ = 'django_celery_beat_crontabschedule'

    id = Column(INTEGER(11), primary_key=True)
    minute = Column(String(240), nullable=False)
    hour = Column(String(96), nullable=False)
    day_of_week = Column(String(64), nullable=False)
    day_of_month = Column(String(124), nullable=False)
    month_of_year = Column(String(64), nullable=False)
    timezone = Column(String(63), nullable=False)


class DjangoCeleryBeatIntervalschedule(Base):
    __tablename__ = 'django_celery_beat_intervalschedule'

    id = Column(INTEGER(11), primary_key=True)
    every = Column(INTEGER(11), nullable=False)
    period = Column(String(24), nullable=False)


class DjangoCeleryBeatPeriodictasks(Base):
    __tablename__ = 'django_celery_beat_periodictasks'

    ident = Column(SMALLINT(6), primary_key=True)
    last_update = Column(DATETIME(fsp=6), nullable=False)


class DjangoCeleryBeatSolarschedule(Base):
    __tablename__ = 'django_celery_beat_solarschedule'
    __table_args__ = (
        Index('django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq', 'event', 'latitude', 'longitude', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    event = Column(String(24), nullable=False)
    latitude = Column(DECIMAL(9, 6), nullable=False)
    longitude = Column(DECIMAL(9, 6), nullable=False)


class DjangoCeleryResultsChordcounter(Base):
    __tablename__ = 'django_celery_results_chordcounter'

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(String(255), nullable=False, unique=True)
    sub_tasks = Column(LONGTEXT, nullable=False)
    count = Column(INTEGER(10), nullable=False)


class DjangoCeleryResultsGroupresult(Base):
    __tablename__ = 'django_celery_results_groupresult'

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(String(255), nullable=False, unique=True)
    date_created = Column(DATETIME(fsp=6), nullable=False, index=True)
    date_done = Column(DATETIME(fsp=6), nullable=False, index=True)
    content_type = Column(String(128), nullable=False)
    content_encoding = Column(String(64), nullable=False)
    result = Column(LONGTEXT)


class DjangoCeleryResultsTaskresult(Base):
    __tablename__ = 'django_celery_results_taskresult'

    id = Column(INTEGER(11), primary_key=True)
    task_id = Column(String(255), nullable=False, unique=True)
    status = Column(String(50), nullable=False, index=True)
    content_type = Column(String(128), nullable=False)
    content_encoding = Column(String(64), nullable=False)
    result = Column(LONGTEXT)
    date_done = Column(DATETIME(fsp=6), nullable=False, index=True)
    traceback = Column(LONGTEXT)
    meta = Column(LONGTEXT)
    task_args = Column(LONGTEXT)
    task_kwargs = Column(LONGTEXT)
    task_name = Column(String(255), index=True)
    worker = Column(String(100), index=True)
    date_created = Column(DATETIME(fsp=6), nullable=False, index=True)
    periodic_task_name = Column(String(255))


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'

    id = Column(BIGINT(20), primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DATETIME(fsp=6), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(LONGTEXT, nullable=False)
    expire_date = Column(DATETIME(fsp=6), nullable=False, index=True)


class NotificationsAppBroadcastnotification(Base):
    __tablename__ = 'notifications_app_broadcastnotification'

    id = Column(BIGINT(20), primary_key=True)
    message = Column(LONGTEXT, nullable=False)
    broadcast_on = Column(DATETIME(fsp=6), nullable=False)
    sent = Column(TINYINT(1), nullable=False)


class RelatoriosCoddanatureza(Base):
    __tablename__ = 'relatorios_coddanatureza'

    id = Column(BIGINT(20), primary_key=True)
    cod_natureza = Column(String(100), nullable=False)


class UploaderFile(Base):
    __tablename__ = 'uploader_file'

    id = Column(BIGINT(20), primary_key=True)
    existingPath = Column(String(100), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    eof = Column(TINYINT(1), nullable=False)
    dt_criacao = Column(DATETIME(fsp=6))


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), nullable=False)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id', unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AuthUser')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(INTEGER(11), primary_key=True)
    action_time = Column(DATETIME(fsp=6), nullable=False)
    object_id = Column(LONGTEXT)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SMALLINT(5), nullable=False)
    change_message = Column(LONGTEXT, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), index=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AuthUser')


class DjangoCeleryBeatPeriodictask(Base):
    __tablename__ = 'django_celery_beat_periodictask'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    task = Column(String(200), nullable=False)
    args = Column(LONGTEXT, nullable=False)
    kwargs = Column(LONGTEXT, nullable=False)
    queue = Column(String(200))
    exchange = Column(String(200))
    routing_key = Column(String(200))
    expires = Column(DATETIME(fsp=6))
    enabled = Column(TINYINT(1), nullable=False)
    last_run_at = Column(DATETIME(fsp=6))
    total_run_count = Column(INTEGER(10), nullable=False)
    date_changed = Column(DATETIME(fsp=6), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    crontab_id = Column(ForeignKey('django_celery_beat_crontabschedule.id'), index=True)
    interval_id = Column(ForeignKey('django_celery_beat_intervalschedule.id'), index=True)
    solar_id = Column(ForeignKey('django_celery_beat_solarschedule.id'), index=True)
    one_off = Column(TINYINT(1), nullable=False)
    start_time = Column(DATETIME(fsp=6))
    priority = Column(INTEGER(10))
    headers = Column(LONGTEXT, nullable=False)
    clocked_id = Column(ForeignKey('django_celery_beat_clockedschedule.id'), index=True)
    expire_seconds = Column(INTEGER(10))

    clocked = relationship('DjangoCeleryBeatClockedschedule')
    crontab = relationship('DjangoCeleryBeatCrontabschedule')
    interval = relationship('DjangoCeleryBeatIntervalschedule')
    solar = relationship('DjangoCeleryBeatSolarschedule')


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id', unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id', unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AuthUser')
