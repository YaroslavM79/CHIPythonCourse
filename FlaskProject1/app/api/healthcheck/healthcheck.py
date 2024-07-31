from flask import jsonify

from app.resources.rest_api_server import RestApiServer

__all__ = ['HealthCheck']


class HealthCheck(RestApiServer):
    """
    Simple view of the project version
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def query_class(self):
        return None

    def get(self):
        result = {'status': 'ok'}
        return jsonify(result)
