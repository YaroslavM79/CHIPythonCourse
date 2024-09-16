from functools import wraps
from flask import request, jsonify

from app.models import Article
from app.models.user import User


def get_current_user_id():
    """Retrieve the current user ID from the request.

    This is a placeholder function. In a real application,
    you would extract the user ID from a JWT token or session.
    """
    user_id = request.headers.get('User-ID')
    if user_id:
        return int(user_id)
    return None


def role_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = get_current_user_id()
            if not user_id:
                return jsonify({'message': 'Authentication required'}), 401
            user = User.query.get(user_id)
            if not user:
                return jsonify({'message': 'User not found'}), 404
            if user.role.name not in required_roles:
                return jsonify({'message': 'Permission denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def article_permission_required(allowed_roles=None, allow_author=False, require_roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Authentication and user retrieval
            user_id = get_current_user_id()
            if not user_id:
                return jsonify({'message': 'Authentication required'}), 401
            user = User.query.get(user_id)
            if not user:
                return jsonify({'message': 'User not found'}), 404

            # General role requirement check
            if require_roles and user.role.name not in require_roles:
                return jsonify({'message': 'Permission denied'}), 403

            # Article-specific permission check
            article_id = kwargs.get('article_id')
            if not article_id:
                return jsonify({'message': 'Article ID is required'}), 400

            article = Article.get_by_id(article_id)
            if not article:
                return jsonify({'message': 'Article not found'}), 404

            has_permission = False
            if allowed_roles and user.role.name in allowed_roles:
                has_permission = True
            if allow_author and user.id == article.author_id:
                has_permission = True

            if has_permission:
                kwargs['article'] = article
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'Permission denied'}), 403
        return decorated_function
    return decorator
