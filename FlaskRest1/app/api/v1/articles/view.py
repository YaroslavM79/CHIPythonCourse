from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request

from app.api.helpers.authorization import article_permission_required, role_required
from app.models.article import Article
from app.api.helpers.authentication import login_required


__all__ = ['ArticleResources']


class ArticleResources(Resource):

    @swag_from('swagger/get_articles.yml')
    def get(self, *args, **kwargs):
        keyword = request.args.get('keyword', None)

        if keyword:
            articles = Article.search_by_keyword(keyword)
        else:
            articles = Article.get_all_articles()

        return [article.to_dict() for article in articles], 200

    @login_required
    @role_required('admin', 'editor', 'viewer')
    @swag_from('swagger/post_article.yml')
    def post(self, *args, **kwargs):
        data = request.get_json()
        if not data or not all(key in data for key in ('title', 'content')):
            return {'message': 'Missing data'}, 400

        user_id = 1
        article = Article(
            title=data['title'],
            content=data['content'],
            author_id=user_id
        )
        article.save_to_db()
        return {'message': 'Article created', 'id': article.id}, 201
