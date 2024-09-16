from abc import ABCMeta, abstractmethod
from logging import getLogger

from jsonschema import validate, ValidationError

from app.resources.rest_api_server import RestApiServer

__all__ = ['RestComponent']


class RestComponent(metaclass=ABCMeta):
    def __init__(self, rest_app):
        self.logger = getLogger(self.__module__)
        self._rest_app = rest_app  # type: RestApiServer
        self.query_helper = self.query_class() if self.query_class else None

    @property
    @abstractmethod
    def query_class(self):
        """what helper need to be used in class"""
        pass

    @property
    def validation_schema(self) -> dict:
        """Validation rules to verify user input (for instance, received by PUT-endpoint).

        It's being handled by jsonschema package:
         https://pypi.org/project/jsonschema/"""

        return {}

    def validate_json_request(self, schema=None):
        """Validate input and abort request (with 400 code) if it's invalid;
               otherwise, returns request body as a dict"""
        schema = self.validation_schema if schema is None else schema
        body = self._rest_app.request.get_json()

        try:
            validate(instance=body, schema=schema)
        except ValidationError as ve:
            self._rest_app.logger.info(ve)
            self._rest_app.abort(description=ve.message, status=400)

        return body
