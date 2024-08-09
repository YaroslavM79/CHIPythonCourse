from flasgger.utils import swag_from
from app.schemas import UserSchema
from app.resources.rest_api_server import RestApiServer
from app.models.user import User

__all__ = ['Users']


class Users(RestApiServer):

    @swag_from("documentation/users.yaml")
    def get(self):
        users = User.get_all()
        return self.create_response(UserSchema(many=True).dump(users))
