import os
from flask import request, Blueprint
from flask.views import MethodView
from flask import Blueprint, request
from flask_restful import Resource, Api
from flasgger.utils import swag_from
from app.models.user import User
from app.resources.api import api

__all__ = ['ApiUsers']


class ApiUsers(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @swag_from('swagger/get_users.yml')
    def get(self):
        users = User.get_all_users()
        return [{'id': user.id, 'username': user.username, 'role': user.role} for user in users], 200
