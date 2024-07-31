from flask import jsonify

from app.resources.rest_api_server import RestApiServer

__all__ = ['VersionInfo']

VERSION_FILE_PATH = 'version'


class VersionInfo(RestApiServer):
    """
    Simple view of the project version
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = self._load_version()

    @property
    def query_class(self):
        return None

    @staticmethod
    def _load_version() -> str:
        with open(VERSION_FILE_PATH) as file:
            version = file.readline().split('=')[1]

        return version

    def get(self):
        result = {'version': self.version}
        return jsonify(result)
