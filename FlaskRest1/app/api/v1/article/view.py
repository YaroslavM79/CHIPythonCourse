from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request, jsonify
from app.models.article import Article
from app.api.helpers.authorization import role_required, article_permission_required
from app.api.helpers.authentication import login_required


__all__ = ['ArticleResources']


class ArticleResources(Resource):

    @login_required
    @swag_from('swagger/get_articles.yml')
    def get(self, user, article_id=None):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404
        return article.to_dict(), 200

    @login_required
    @article_permission_required(allowed_roles=['admin', 'editor'], allow_author=True)
    @role_required('admin', 'editor', 'viewer')
    @swag_from('swagger/put_article.yml')
    def put(self, user, article_id):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404

        data = request.get_json()
        article.update_in_db(**data)
        return {'message': 'Article updated'}, 200

    @login_required
    @article_permission_required(allowed_roles=['admin'], allow_author=True)
    @role_required('admin', 'viewer', 'editor')
    @swag_from('swagger/delete_article.yml')
    def delete(self, user, article_id):
        article = Article.get_by_id(article_id)
        if not article:
            return {'message': 'Article not found'}, 404

        article.delete_from_db()
        return {'message': 'Article deleted'}, 200
