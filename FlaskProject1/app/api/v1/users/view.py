from flasgger.utils import swag_from
from app.schemas import UserSchema
from app.resources.rest_api_server import RestApiServer
from app.models.user import User
from flask_restful import Resource
from flask import jsonify
from flasgger import Swagger, SwaggerView, Schema, fields

__all__ = ['Users']


class Users(SwaggerView):
    responses = {
        200: {
            "description": "Endpoint returning a list of users",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": UserSchema
                    }
                }
            }
        }
    }

    def get(self):
        """Endpoint returning a list of users
        ---
        """
        users = User.get_all()
        return jsonify(UserSchema(many=True).dump(users))
