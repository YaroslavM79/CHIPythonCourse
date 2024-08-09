from marshmallow import Schema, fields
from app.models.article import Article
from app.models.role import Role
from app.models.user import User

__all__ = ['UserSchema', 'ArticleSchema', 'RoleSchema']


class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    users = fields.List(fields.Nested(lambda: UserSchema(exclude=('role',))), dump_only=True)


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(lambda: UserSchema(exclude=('articles', 'role')), dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    role = fields.Nested(lambda: RoleSchema(exclude=('users',)), dump_only=True)
    articles = fields.List(fields.Nested(lambda: ArticleSchema(exclude=('author',))), dump_only=True)

