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
        }
    }

swagger = Swagger()
