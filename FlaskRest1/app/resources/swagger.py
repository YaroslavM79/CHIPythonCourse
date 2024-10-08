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
    }
}

swagger = Swagger()
