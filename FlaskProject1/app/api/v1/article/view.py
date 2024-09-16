from flask_smorest import Blueprint, abort
from app.models import Article
from app.schemas import ArticleSchema, ArticleIDQuerySchema
from flask.views import MethodView
from flask import request

__all__ = ['ArticleResource']

api_bp = Blueprint('article', 'article', url_prefix='/article', description='Operations on articles')


@api_bp.route('/')
class ArticleResource(MethodView):

    @api_bp.response(200, ArticleSchema(many=True))
    def get(self):
        """Get list of all articles or a single article by ID via query parameter"""
        article_id = request.args.get('article_id')
        if article_id:
            article = Article.find_by_id(article_id)
            if not article:
                abort(404, message="Article not found.")
            return article
        else:
            articles = Article.get_all()
            return articles

    @api_bp.arguments(ArticleSchema)
    @api_bp.response(201, ArticleSchema)
    def post(self, new_article_data):
        """Create a new article"""
        new_article = Article(**new_article_data)
        new_article.save()
        return new_article

    @api_bp.arguments(ArticleIDQuerySchema, location='query')
    @api_bp.arguments(ArticleSchema)
    @api_bp.response(200, ArticleSchema)
    def put(self, query_params, update_article_data):
        """Update an article by ID via query parameter"""
        article_id = query_params['article_id']
        article = Article.find_by_id(article_id)
        if not article:
            abort(404, message="Article not found.")
        article.title = update_article_data['title']
        article.content = update_article_data['content']
        article.save()
        return article

    @api_bp.arguments(ArticleIDQuerySchema, location='query')
    @api_bp.response(204)
    def delete(self, query_params):
        """Delete an article by ID via query parameter"""
        article_id = query_params['article_id']
        article = Article.find_by_id(article_id)
        if not article:
            abort(404, message="Article not found.")
        article.delete()
        return '', 204
