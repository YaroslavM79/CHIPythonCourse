from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request, jsonify
from app.models.article import Article
from app.models.user import User
from app.api.helpers.authentication import role_required, get_current_user_id


__all__ = ['ArticleResources']


class ArticleResources(Resource):

    @swag_from('swagger/get_articles.yml')
    def get(self, article_id):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404
        return article.to_dict(), 200

    @role_required('admin', 'editor', 'viewer')
    @swag_from('swagger/post_article.yml')
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ('title', 'content')):
            return {'message': 'Missing data'}, 400

        user_id = get_current_user_id()
        if not user_id:
            return {'message': 'Authentication required'}, 401

        article = Article(
            title=data['title'],
            content=data['content'],
            author_id=user_id
        )
        article.save_to_db()
        return {'message': 'Article created', 'id': article.id}, 201

    @role_required('admin', 'editor', 'viewer')
    @swag_from('swagger/put_article.yml')
    def put(self, article_id):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404

        user_id = get_current_user_id()
        if not user_id:
            return {'message': 'Authentication required'}, 401

        user = User.get_by_id(user_id)

        # Permission checks
        if user.role.name == 'admin' or \
           (user.role.name == 'editor') or \
           (user.id == article.author_id):
            data = request.get_json()
            article.update_in_db(**data)
            return {'message': 'Article updated'}, 200
        else:
            return {'message': 'Permission denied'}, 403

    @role_required('admin', 'viewer', 'editor')
    @swag_from('swagger/delete_article.yml')
    def delete(self, article_id):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404

        user_id = get_current_user_id()
        if not user_id:
            return {'message': 'Authentication required'}, 401

        user = User.get_by_id(user_id)

        # Permission checks
        if user.role.name == 'admin' or (user.id == article.author_id):
            article.delete_from_db()
            return {'message': 'Article deleted'}, 200
        else:
            return {'message': 'Permission denied'}, 403
