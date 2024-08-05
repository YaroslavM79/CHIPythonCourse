from flasgger.utils import swag_from

from app.resources.rest_api_server import RestApiServer
from app.db_operatios.user_service import UserService

__all__ = ['Users']


class Users(RestApiServer):

    @swag_from("documentation/users.yaml")
    def get(self):
        # data = request.parsed_data.get('args', {})
        users = UserService.get_all_users()
        self.create_response(users)
