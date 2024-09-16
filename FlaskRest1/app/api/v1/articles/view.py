from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request

from app.api.helpers.authentication import article_permission_required, get_current_user_id
from app.models.article import Article

__all__ = ['ArticleResources']


class ArticleResources(Resource):

    @swag_from('swagger/get_articles.yml')
    def get(self):
        articles = Article.get_all_articles()
        return [article.to_dict() for article in articles], 200

    @article_permission_required(require_roles=['admin', 'editor', 'viewer'])
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
