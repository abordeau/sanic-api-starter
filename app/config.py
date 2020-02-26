import os

from sanic_envconfig import EnvConfig

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(ROOT, os.pardir))
STATIC_DIR = os.path.abspath(os.path.join(ROOT, 'static'))
APP_DIR = os.path.abspath(os.path.join(ROOT, 'app'))


class Config(EnvConfig):
    DEBUG: bool = True
    POOL_MAX_CONNECTIONS: int = 2
