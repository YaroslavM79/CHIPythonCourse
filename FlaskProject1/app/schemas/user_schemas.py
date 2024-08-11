from marshmallow import fields
from app.resources.marshmallow import ma
from app.models import User, Article, Role

__all__ = ['UserIDQuerySchema', 'UserCreateSchema']


class UserIDQuerySchema(ma.Schema):
    user_id = fields.Int(required=True, description="ID of the user")


class UserCreateSchema(ma.Schema):
    username = ma.Str(required=True)
    email = ma.Email(required=True)
    role_id = ma.Int(required=True)
