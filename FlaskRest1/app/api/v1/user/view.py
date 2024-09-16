from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request

from app.api.helpers.authentication import role_required
from app.models.role import Role
from app.models.user import User

__all__ = ['UserResources']


class UserResources(Resource):

    @role_required('admin', 'editor')
    @swag_from('swagger/get_user.yml')
    def get(self, user_id=None):
        if user_id:
            user = User.get_by_id(user_id)
            if user is None:
                return {'message': 'User not found'}, 404
            return user.to_dict(), 200
        else:
            users = User.get_all_users()
            return [user.to_dict() for user in users], 200

    @role_required('admin')
    @swag_from('swagger/put_user.yml')
    def put(self, user_id):
        user = User.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        data = request.get_json()
        if 'role' in data:
            role = Role.get_by_name(data['role'])
            if not role:
                return {'message': f"Role '{data['role']}' does not exist"}, 400
            data['role_id'] = role.id
            del data['role']
        user.update_in_db(**data)
        return {'message': 'User updated'}, 200

    @role_required('admin')
    @swag_from('swagger/delete_user.yml')
    def delete(self, user_id):
        user = User.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted'}, 200