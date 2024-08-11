from app.models import User
from app.schemas import UserSchema, UserIDQuerySchema, UserCreateSchema
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request

__all__ = ['UserResource']

api_bp = Blueprint('User', 'user', url_prefix='/user', description='Operations on users')


@api_bp.route('/')
class UserResource(MethodView):

    @api_bp.response(200, UserSchema(many=True))
    def get(self):
        """Get list of all users or a single user by ID"""
        user_id = request.args.get('user_id')
        if user_id:
            user = User.find_by_id(user_id)
            if not user:
                abort(404, message="User not found.")
            return user
        else:
            users = User.get_all()
            return users

    @api_bp.arguments(UserCreateSchema)
    @api_bp.response(201, UserSchema)
    def post(self, new_data):
        """Create a new user"""
        if User.query.filter_by(username=new_data['username']).first():
            abort(400, message="A user with that username already exists.")

        new_user = User(**new_data)
        new_user.save()
        return new_user

    @api_bp.arguments(UserCreateSchema)
    @api_bp.response(200, UserSchema)
    def put(self, update_data):
        """Update an existing user by ID"""
        user_id = update_data.get('id')
        user = User.find_by_id(user_id)
        if not user:
            abort(404, message="User not found.")

        user.username = update_data['username']
        user.email = update_data['email']
        user.role_id = update_data['role_id']
        user.save()
        return user

    @api_bp.arguments(UserIDQuerySchema, location='query')
    @api_bp.response(204)
    def delete(self, query_params):
        """Delete a user by ID"""
        user_id = query_params['user_id']
        user = User.find_by_id(user_id)
        if not user:
            abort(404, message="User not found.")
        user.delete()
        return '', 204
