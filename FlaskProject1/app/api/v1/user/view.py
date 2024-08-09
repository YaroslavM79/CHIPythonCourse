from flasgger.utils import swag_from
from flask_restful import abort

from app.resources.rest_api_server import RestApiServer
from app.db_operatios.user_service import UserService
from app.schemas import UserSchema

__all__ = ['User']

user_schema = UserSchema()


class User(RestApiServer):
    # @swag_from("documentation/get_user.yaml")
    def get(self, id):
        user = UserService.get_user_by_id(id)
        if user:
            return self.create_response(user)
        return abort(404, description={'message': 'User not found'})

    # @swag_from("documentation/get_user.yaml")
    def post(self):
        pass
        # data = request.get_json()
        # new_user = UserService.create_user(data)
        # return jsonify(new_user), 201

    # @swag_from('documentation/update_user.yaml')
    def put(self, id):
        pass
        # data = request.get_json()
        # updated_user = UserService.update_user(id, data)
        # if updated_user:
        #     return jsonify(updated_user)

    # @swag_from('documentation/delete_user.yaml')
    def delete(self, id):
        result = UserService.delete_user(id)
        return self.create_response({'message': 'User deleted'})
