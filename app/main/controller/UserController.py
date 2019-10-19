from flask import request
from flask_restplus import Resource

from ..models.dto.UserDto import UserDto
from ..service.UserService import UserService

api = UserDto.api
userDto = UserDto.user
sv = UserService()

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(userDto, envelope='data')
    def get(self):
        return sv.findAll()

    @api.expect(userDto, validate=True)
    @api.response(201, 'User successfully created')
    @api.doc('Create a new user')
    def post(self):
        data = request.json
        return sv.create(data=data)


@api.route('/<username>')
@api.param('username', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('Find user by username')
    @api.marshal_with(userDto)
    def get(self, username):
        user = sv.findByUserName(username)
        if not user:
            api.abort(404)
        else:
            return user