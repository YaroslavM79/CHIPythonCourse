from flasgger import Swagger



SWAGGER_DEFINITIONS = {
        'User': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer'
                },
                'username': {
                    'type': 'string'
                },
                'role': {
                    'type': 'string'
                }
            }
        }
    }

swagger = Swagger()
