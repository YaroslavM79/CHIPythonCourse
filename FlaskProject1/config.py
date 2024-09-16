"""
classes that containing settings variables for all environments.
"""
import os
from blueprints_config import SYSTEM_APP_BLUEPRINTS, SUPPORTED_APP_V1_BLUEPRINTS, DEBUG_APP_BLUEPRINTS, TEST_APP_BLUEPRINTS

__all__ = ['ProductionConfig', 'DevelopmentConfig', 'TestingConfig']


class BaseConfig:
    """
    Base config for project
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'

    DB_HOSTNAME = os.environ.get('DB_HOSTNAME', 'postgres')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASS = os.environ.get('DB_PASS', 'postgres')
    DB_NAME = os.environ.get('DB_NAME', 'test_db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        DB_USER,
        DB_PASS,
        DB_HOSTNAME,
        DB_PORT,
        DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 0
    SQLALCHEMY_POOL_TIMEOUT = 100

    # level loggings
    LOG_LEVEL = 'debug'

    # Blueprints defaults
    DEFAULT_ITEMS_PER_PAGE = 50

    FLASK_ENV = "production"
    FLASK_DEBUG = False
    TESTING = False

    API_TITLE = 'Flask app api 1'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/api/v1'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    SYSTEM_BLUEPRINTS = SYSTEM_APP_BLUEPRINTS

    @property
    def BLUEPRINT_CONFIG(self):
        """
        return all blueprint config available for particular environment
        """
        return self._blueprint_config

    def __init__(self):
        self._blueprint_config = list()
        self._blueprint_config.extend(SUPPORTED_APP_V1_BLUEPRINTS)


class ProductionConfig(BaseConfig):
    """Production configuration options."""
    LOG_LEVEL = 'error'
    PROPAGATE_EXCEPTIONS = True

    def __init__(self):
        super().__init__()


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
        self._blueprint_config.extend(DEBUG_APP_BLUEPRINTS)
        self._blueprint_config.extend(TEST_APP_BLUEPRINTS)


class TestingConfig(BaseConfig):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
    LOG_LEVEL = 'info'
    PROPAGATE_EXCEPTIONS = True

    def __init__(self):
        super().__init__()
        self._blueprint_config.extend(DEBUG_APP_BLUEPRINTS)
        self._blueprint_config.extend(TEST_APP_BLUEPRINTS)
