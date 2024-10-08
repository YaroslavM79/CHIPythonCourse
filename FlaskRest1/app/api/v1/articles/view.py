from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request

from app.api.helpers.authentication import article_permission_required, role_required, get_current_user_id
from app.models.article import Article

__all__ = ['ArticleResources']


class ArticleResources(Resource):

    @swag_from('swagger/get_articles.yml')
    def get(self):
        articles = Article.get_all_articles()
        return [article.to_dict() for article in articles], 200
