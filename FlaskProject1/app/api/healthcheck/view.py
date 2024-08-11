from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify

__all__ = ['HealthCheck']

api_bp = Blueprint('health_check', 'health_check', url_prefix='/health_check', description='Health check endpoint')


@api_bp.route('/')
class HealthCheck(MethodView):
    """
    Simple view for checking the health of the service
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api_bp.response(200)
    def get(self):
        """Return the health status of the service"""
        result = {'status': 'ok'}
        return jsonify(result)
