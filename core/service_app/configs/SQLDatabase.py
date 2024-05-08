# noinspection PyUnresolvedReferences
import asyncio
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from core.service_app.configs.Logger import get_logger_gn
from core.service_app.configs.Settings import get_settings_gn

async_engines_dict = dict()


def async_db_engine(pool_size=2, settings=Depends(get_settings_gn)):
    if async_engines_dict.get(pool_size):
        return async_engines_dict.get(pool_size)
    eng = create_async_engine(settings.SQL_DSN, pool_pre_ping=True, pool_size=pool_size, echo=False, )
    async_engines_dict[pool_size] = eng
    return eng


def async_db_session(pool_size=2, logger=Depends(get_logger_gn(__name__))) -> AsyncSession:
    try:
        engine = async_db_engine(pool_size)
        async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)()
        return async_session
    except Exception as e:
        logger.error("async_db_session", error=e)


engines_dict = dict()


def db_engine(pool_size=2, settings=Depends(get_settings_gn)):
    if engines_dict.get(pool_size):
        return engines_dict.get(pool_size)
    eng = create_engine(settings.SQL_DSN, pool_pre_ping=True,
                        pool_recycle=10000, pool_size=pool_size)
    engines_dict[pool_size] = eng
    return eng


def db_session(pool_size=2, logger=Depends(get_logger_gn(__name__))) -> Session:
    try:
        engine = db_engine(pool_size)
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))()
        return session
    except Exception as e:
        logger.error("db_session", error=e)


