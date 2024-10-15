from flask import Flask

from app.resources.api_config import ApiConfig
from config import DevelopmentConfig
from app.resources.db import db
from app.resources.api import api
from app.resources.swagger import swagger, SWAGGER_DEFINITIONS, SECURITY_DEFINITIONS

__all__ = ['AppCreator']


class AppCreator:
    def __init__(self):
        self.app = Flask(__name__)
        #TODO: get it from env
        self.app.config.from_object(DevelopmentConfig())
        self._register_extensions()
        self._register_blueprints()

    def _register_db(self):
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def _register_api(self):
        api.init_app(app=self.app)
        api.app = self.app

    def _register_swagger(self):
        self.app.config['SWAGGER'] = {
            'title': 'Test APP',
            'uiversion': 3,
            'definitions': SWAGGER_DEFINITIONS,
            'securityDefinitions': SECURITY_DEFINITIONS,
        }

        swagger.init_app(app=self.app)

    def _register_extensions(self):
        self._register_db()
        self._register_api()
        self._register_swagger()

    def _register_blueprints(self):
        ApiConfig(rest_app=self.app, bp_config=self.app.config['BLUEPRINT_CONFIG'], api_prefix=self.app.config['OPENAPI_URL_PREFIX'])

    def get_app(self):
        return self.app

