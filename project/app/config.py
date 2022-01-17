import imp
import logging
import os

from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = os.getenv('ENVIRONMENT', 'dev')
    testing: bool = bool(os.getenv('TESTING', 0))

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment.....')
    return Settings()
