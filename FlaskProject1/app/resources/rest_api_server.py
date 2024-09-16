import logging

from flask.views import MethodView


__all__ = ['RestApiServer']


class RestApiServer(MethodView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    # def create_response(self, data: dict, status_code: int = 200, headers=None,
    #                     output_type: str = ProjectConstants.JSON):
    #     output_type_class = {
    #         ProjectConstants.JSON: RestApiServer.output_json,
    #         ProjectConstants.CSV: RestApiServer.output_csv,
    #         ProjectConstants.ZIP: RestApiServer.output_zip,
    #     }
    #     fn = output_type_class.get(output_type)
    #     result = fn(data=data, status_code=status_code, headers=headers)
    #     return result
    #
    # @staticmethod
    # @api.representation('application/json')
    # def output_json(data, status_code, headers=None):
    #     response = jsonify(data)
    #     response.status_code = status_code
    #     response.headers.extend(headers or {})
    #     return response
    #
    # @staticmethod
    # @api.representation('text/csv')
    # def output_csv(data, status_code, headers=None):
    #     response = make_response(data)
    #     response.status_code = status_code
    #     response.headers.extend(headers or {})
    #     return response
    #
    # @staticmethod
    # @api.representation('application/zip')
    # def output_zip(data, status_code, headers=None):
    #     response = make_response(data)
    #     response.status_code = status_code
    #     response.headers.extend(headers or {})
    #     return response
