from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('User', description='User related operations')
    user = api.model('user', {
        'id': fields.String(description='user Identifier'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })