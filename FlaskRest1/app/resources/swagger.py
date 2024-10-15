from flasgger import Swagger

SWAGGER_DEFINITIONS = {
    'User': {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'username': {'type': 'string'},
            'role': {'type': 'string'}
        }
    },
    'NewUser': {
        'type': 'object',
        'required': ['username', 'password', 'role'],
        'properties': {
            'username': {'type': 'string'},
            'password': {'type': 'string'},
            'role': {'type': 'string'}
        }
    },
    'UpdateUser': {
        'type': 'object',
        'properties': {
            'username': {'type': 'string'},
            'password': {'type': 'string'},
            'role': {'type': 'string'}
        }
    },
    'Article': {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'title': {'type': 'string'},
            'content': {'type': 'string'},
            'author': {'$ref': '#/definitions/User'},
            'created_at': {
                'type': 'string',
                'format': 'date-time'
            }
        }
    },
    'NewArticle': {
        'type': 'object',
        'required': ['title', 'content'],
        'properties': {
            'title': {'type': 'string'},
            'content': {'type': 'string'}
        }
    },
    'UpdateArticle': {
        'type': 'object',
        'properties': {
            'title': {'type': 'string'},
            'content': {'type': 'string'}
        }
    },
    'BasicAuth': {
        'type': 'http',
        'scheme': 'basic'
    },
    'Error401': {
        'description': 'Authentication required or invalid credentials',
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'Missing username or password'
                        }
                    }
                }
            }
        }
    },
    'UserError404': {
        'description': 'User not found',
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {
                            'type': 'string',
                            'example': 'User not found'
                        }
                    }
                }
            }
        }
    }
}

SECURITY_DEFINITIONS = {
        'basicAuth': {
            'type': 'basic',
            'description': 'Basic HTTP Authentication using username and password.'
        }
}

swagger = Swagger()
