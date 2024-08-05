from flasgger.utils import swag_from
from flask_restful import abort

from app.resources.rest_api_server import RestApiServer
from app.db_operatios.user_service import UserService

__all__ = ['Articles']


class Articles(RestApiServer):
    @swag_from("documentation/get_user.yaml")
    def get(self, id):
        user = UserService.get_user_by_id(id)
        if user:
            return self.create_response(user)
        return abort(404, description={'message': 'User not found'})
