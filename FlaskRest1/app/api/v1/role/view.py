from flask_restful import Resource
from flasgger.utils import swag_from
from flask import request
from app.models.role import Role
from app.api.helpers.authentication import role_required

__all__ = ['RoleResources']


class RoleResources(Resource):

    @role_required('admin')
    @swag_from('swagger/get_roles.yml')
    def get(self):
        roles = Role.get_all_roles()
        return [role.to_dict() for role in roles], 200

    @role_required('admin')
    @swag_from('swagger/post_role.yml')
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data:
            return {'message': 'Missing role name'}, 400
        try:
            role = Role.create_role(data['name'])
        except ValueError as e:
            return {'message': str(e)}, 400
        return {'message': 'Role created', 'id': role.id}, 201

    @role_required('admin')
    @swag_from('swagger/delete_role.yml')
    def delete(self, role_id):
        success = Role.delete_role(role_id)
        if not success:
            return {'message': 'Role not found'}, 404
        return {'message': 'Role deleted'}, 200
