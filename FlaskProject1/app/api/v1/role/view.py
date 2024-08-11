from flask_smorest import Blueprint, abort
from app.models import Role
from app.schemas import RoleSchema, RoleIDQuerySchema
from flask.views import MethodView
from flask import request

__all__ = ['RoleResource']

api_bp = Blueprint('roles', 'roles', url_prefix='/roles', description='Operations on roles')


@api_bp.route('/')
class RoleResource(MethodView):

    @api_bp.response(200, RoleSchema(many=True))
    def get(self):
        """Get list of all roles or a single role by ID via query parameter"""
        role_id = request.args.get('role_id')
        if role_id:
            role = Role.find_by_id(role_id)
            if not role:
                abort(404, message="Role not found.")
            return role
        else:
            roles = Role.get_all()
            return roles

    @api_bp.arguments(RoleSchema)
    @api_bp.response(201, RoleSchema)
    def post(self, new_role_data):
        """Create a new role"""
        new_role = Role(**new_role_data)
        new_role.save()
        return new_role

    @api_bp.arguments(RoleIDQuerySchema, location='query')
    @api_bp.arguments(RoleSchema)
    @api_bp.response(200, RoleSchema)
    def put(self, query_params, update_role_data):
        """Update a role by ID via query parameter"""
        role_id = query_params['role_id']
        role = Role.find_by_id(role_id)
        if not role:
            abort(404, message="Role not found.")
        role.name = update_role_data['name']
        role.save()
        return role

    @api_bp.arguments(RoleIDQuerySchema, location='query')
    @api_bp.response(204)
    def delete(self, query_params):
        """Delete a role by ID via query parameter"""
        role_id = query_params['role_id']
        role = Role.find_by_id(role_id)
        if not role:
            abort(404, message="Role not found.")
        role.delete()
        return '', 204
