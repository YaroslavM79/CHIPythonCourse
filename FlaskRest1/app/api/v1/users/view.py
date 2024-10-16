from flask import request
from flask_restful import Resource
from flasgger.utils import swag_from

from app.api.helpers.authorization import role_required
from app.api.helpers.authentication import login_required
from app.models.role import Role
from app.models.user import User

__all__ = ['ApiUsers']


class ApiUsers(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @login_required
    @role_required('admin')
    @swag_from('swagger/get_users.yml')
    def get(self, *args, **kwargs):
        keyword = request.args.get('keyword', None)
        if keyword:
            users = User.search_by_keyword(keyword)
        else:
            users = User.get_all_users()

        return [{'id': user.id, 'username': user.username, 'role': user.user_role.name} for user in users], 200

    @login_required
    @role_required('admin')
    @swag_from('swagger/post_user.yml')
    def post(self, *args, **kwargs):
        data = request.get_json()
        if not data or not all(key in data for key in ('username', 'password', 'role')):
            return {'message': 'Missing data'}, 400
        if User.get_by_username(data['username']):
            return {'message': 'User already exists'}, 409
        role = Role.get_by_name(data['role'])
        if not role:
            return {'message': f"Role '{data['role']}' does not exist"}, 400
        user = User(username=data['username'], password=data['password'], role_id=role.id)
        user.save_to_db()
        return {'message': 'User created', 'id': user.id}, 201
