from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify
import os

__all__ = ['VersionInfo']

VERSION_FILE_PATH = os.path.join(os.path.dirname(__file__), 'version.txt')

api_bp = Blueprint('version_info', 'version_info', url_prefix='/version_info', description='Project version information')


@api_bp.route('/')
class VersionInfo(MethodView):
    """
    Simple view of the project version
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = self._load_version()

    @staticmethod
    def _load_version() -> str:
        with open(VERSION_FILE_PATH) as file:
            version = file.readline().split('=')[1].strip()
        return version

    @api_bp.response(200)
    def get(self):
        """Return the current project version"""
        result = {'version': self.version}
        return jsonify(result)
