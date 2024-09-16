from marshmallow import fields
from app.resources.marshmallow import ma
from app.models import User, Article, Role

__all__ = ['ArticleSchema', 'RoleSchema', 'UserSchema']


class ArticleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Article
        load_instance = True

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Nested(lambda: UserSchema(exclude=('articles', 'role')), dump_only=True)


class RoleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Role
        load_instance = True

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    users = fields.List(fields.Nested(lambda: UserSchema(exclude=('role',))), dump_only=True)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    role = fields.Nested(lambda: RoleSchema(exclude=('users',)), dump_only=True)
    articles = fields.List(fields.Nested(lambda: ArticleSchema(exclude=('author',))), dump_only=True)

