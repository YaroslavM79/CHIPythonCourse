from functools import wraps
from flask import request, jsonify

from app.models.article import Article
from app.models.user import User


def role_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(user=None, *args, **kwargs):

            if user.user_role.name not in required_roles:
                return {'message': 'Permission denied'}, 403

            return f(user, *args, **kwargs)
        return decorated_function
    return decorator


def article_permission_required(allowed_roles=None, allow_author=False):
    allowed_roles = allowed_roles or []
    def decorator(f):
        @wraps(f)
        def decorated_function(user=None, *args, **kwargs):
            article_id = kwargs.get('article_id')
            if not article_id:
                return {'message': 'Article ID is required'}, 400

            article = Article.query.get(article_id)
            if not article:
                return {'message': 'Article not found'}, 404

            if allow_author and article.author_id == user.id:
                return f(*args, **kwargs)

            if user.user_role.name not in allowed_roles:
                return {'message': 'Permission denied'}, 403

            return f(user, *args, **kwargs)
        return decorated_function
    return decorator
