import json
import logging
import traceback
import importlib

from flask import Flask, jsonify
from flask import Response

from app.resources.db import db
from app.resources.logger import Logger
from app.resources.api_config import ApiConfig
from app.resources.rest_api import api
from app.resources.config_manager import ConfigManager
<<<<<<< HEAD

=======
from app.resources.swagger import generate_template
from flask_cors import CORS
>>>>>>> 00bf3f0251235c4e81305227ef7887b5f84564da

try:
    from http import HTTPStatus
except ImportError:
    import httplib as HTTPStatus

__all__ = ['create_app']

server_logger = logging.getLogger("server.py")


def create_app():
    """Create pre-configured Flask-based application

    :return: RestServerApi-object
        :rtype RestServerApi
    """
    config_manager = ConfigManager()

    app = Flask(__package__)
    app.url_map.strict_slashes = False

    CORS(app)

    module_name = config_manager.app_settings
    setting_class = getattr(importlib.import_module("config"), module_name)
    config_settings = setting_class()
    app.config.from_object(config_settings)

    # initialization of extension instances
    db.init_app(app=app)
    # db.reflect(app=app)
    # with app.app_context():
    #     db.Model.metadata.reflect(db.engine)

    # setting up logging
    log_level = app.config['LOG_LEVEL']
    logger = Logger(log_level)
    log = logging.getLogger('werkzeug')
    log.setLevel(logger.log_level)
    sql_log = logging.getLogger('sqlalchemy.engine')
    sql_log.setLevel(logger.log_level)

<<<<<<< HEAD
=======
    template = generate_template(app=app)

    # Swagger(app=app, parse=True, template=template, validation_error_handler=validation_handler)
    Swagger(app=app, parse=True, template=template, validation_error_handler=validation_handler)

    # register all rest endpoints resources
    ApiConfig(rest_app=app, bp_config=app.config['BLUEPRINT_CONFIG'])

>>>>>>> 00bf3f0251235c4e81305227ef7887b5f84564da
    # Initialize api with created resources
    # api.prefix = app.config['API_PREFIX']
    api.init_app(app=app)
    api.app = app

    # register all rest endpoints resources
    # ApiConfig(rest_app=app, bp_config=app.config['BLUEPRINT_CONFIG'])
    ApiConfig(bp_config=app.config['SYSTEM_BLUEPRINTS'])
    ApiConfig(bp_config=app.config['BLUEPRINT_CONFIG'], api_prefix=app.config['OPENAPI_URL_PREFIX'])

    for rule in app.url_map.iter_rules():
        print(f"Endpoint: {rule.endpoint}, URL: {rule}")

    return app


def get_traceback(ex: Exception):
    """ print exception stacktrace"""
    lines = traceback.format_exception(type(ex), ex, ex.__traceback__)
    return ''.join(lines)


def _set_server_error_handler_callbacks(app):
    """register callbacks handle errors"""

    @app.errorhandler(Exception)
    def handle_exception(ex: Exception):
        logging.error(get_traceback(ex))
        return jsonify({"errors": str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
