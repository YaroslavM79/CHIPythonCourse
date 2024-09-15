from flasgger import APISpec, Schema, Swagger, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

# Create an APISpec
from app.schemas import UserSchema

spec = APISpec(
    title='The Flask API 1',
    version='1.0.0',
    openapi_version='3.0.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


def generate_template(app):
    # spec.components.schemas('User', schema=UserSchema)

    template = spec.to_flasgger(app=app)
    return template
