"""
classes that containing settings variables for all environments.
"""
import os

from blueprints_config import SYSTEM_APP_BLUEPRINTS, SUPPORTED_APP_V1_BLUEPRINTS


class BaseConfig:
    """
    Base config for project
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'

    DB_HOSTNAME = os.environ.get('DB_HOSTNAME', 'postgres')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'test_db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        DB_HOSTNAME,
        DB_PORT,
        POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 0
    SQLALCHEMY_POOL_TIMEOUT = 100

    # level loggings
    LOG_LEVEL = 'debug'

    # Blueprints defaults
    DEFAULT_ITEMS_PER_PAGE = 50

    # api prefix for all endpoints.
    # API_PREFIX = '/api'
    OPENAPI_URL_PREFIX = '/api/v1'
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    TESTING = False

    @property
    def BLUEPRINT_CONFIG(self):
        """
        return all blueprint config available for particular environment
        """
        return self._blueprint_config

    def __init__(self):
        self._blueprint_config = dict()
        self._blueprint_config.update(SYSTEM_APP_BLUEPRINTS)
        self._blueprint_config.update(SUPPORTED_APP_V1_BLUEPRINTS)


class DevelopmentConfig(BaseConfig):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False
    LOG_LEVEL = 'info'
    USERS_PER_PAGE = 50
    FLASK_ENV = "development"
    PROPAGATE_EXCEPTIONS = True

    def __init__(self):
        super().__init__()

