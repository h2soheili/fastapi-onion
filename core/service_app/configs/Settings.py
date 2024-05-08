import secrets
from typing import (List, Optional)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    PORT: Optional[int] = 0
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    BACKEND_CORS_ORIGINS: List[str] = []
    REDIS_DSN: Optional[str] = None

    OBJECT_STORAGE_URL: Optional[str] = ''
    OBJECT_STORAGE_ACCESS_KEY: Optional[str] = ''
    OBJECT_STORAGE_SECRET_KEY: Optional[str] = ''

    LOG_LEVEL: Optional[str] = "DEBUG"

    SQL_DSN: Optional[str] = None

    model_config = SettingsConfigDict(env_file='.env.dev', env_file_encoding='utf-8', extra='allow')


settings: Optional[Settings] = None


def load_settings(env_str):
    global settings
    env_file = f".env.{env_str}"
    settings = Settings(_env_file=env_file)


async def get_settings_gn():
    yield settings


def get_settings():
    return settings
