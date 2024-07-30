import decimal
import json
import logging
import traceback

import requests
from flasgger import Swagger
from flask import Flask, jsonify
from flask import Response
from flask_restful import abort
from .rest_api import api

try:
    from http import HTTPStatus
except ImportError:
    import httplib as HTTPStatus

__all__ = ['create_app']

server_logger = logging.getLogger("server.py")


def validation_handler(error, _data, _schema):
    """
    Custom validation error handler which produces 404 Bad Request
    response in case validation fails and returns the error
    """
    error_parameters = ", ".join(error.path)
    error_dict = json.dumps(
        {'errors': f'{error_parameters} {error.message}'})
    abort(Response(error_dict, status=HTTPStatus.BAD_REQUEST))


def create_app():
    """Create pre-configured Flask-based application

    :return: RestServerApi-object
        :rtype RestServerApi
    """

    app = Flask(__package__)
    app.url_map.strict_slashes = False

    # initialization of extension instances
    db.init_app(app=app)
    db.reflect(app=app)
    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    # setting up logging
    log_level = app.config['LOG_LEVEL']
    logger = Logger(log_level)
    log = logging.getLogger('werkzeug')
    log.setLevel(logger.log_level)
    sql_log = logging.getLogger('sqlalchemy.engine')
    sql_log.setLevel(logger.log_level)
    Swagger(app=app, parse=True, validation_error_handler=validation_handler)

    # register all rest endpoints resources
    ApiConfig(rest_app=app, bp_config=app.config['BLUEPRINT_CONFIG'])

    # Initialize api with created resources
    api.prefix = app.config['API_PREFIX']
    api.init_app(app=app)
    api.app = app

    class JsonEncoder(app.json_encoder):
        """A class to represent json correctly"""

        def default(self, obj, *_args, **_kwargs):
            """handle objects for json"""
            if isinstance(obj, decimal.Decimal):
                return float(obj)
            if hasattr(obj, 'to_dict') and callable(obj.to_dict):
                return obj.to_dict()
            else:
                return super().default(obj)

    app.json_encoder = JsonEncoder

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
