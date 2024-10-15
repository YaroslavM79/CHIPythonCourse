from functools import wraps
from flask import request, jsonify
from app.models import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {'message': 'Missing username or password'}, 401

        user = User.get_by_username(auth.username)
        if not user:
            return {'message': 'User not found'}, 404

        if not user.check_password(auth.password):
            return {'message': 'Invalid password'}, 401

        return f(user, *args, **kwargs)

    return decorated_function
