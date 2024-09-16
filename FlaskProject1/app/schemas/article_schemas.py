from marshmallow import fields
from app.resources.marshmallow import ma
from app.models import User, Article, Role

from marshmallow import Schema, fields

__all__ = ['ArticleIDQuerySchema']


class ArticleIDQuerySchema(Schema):
    article_id = fields.Int(required=True, description="The ID of the article")

