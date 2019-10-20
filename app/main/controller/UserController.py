from flask import request
from flask_restplus import Resource

from ..models.dto.UserDto import UserDto
from ..service.UserService import UserService

api = UserDto.api
userDto = UserDto.user
sv = UserService()

@api.route('/')
@api.response(404, 'User not found.')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(userDto, envelope='data')
    def get(self):
        """
        Return list of users
        """
        return sv.findAll()

    @api.expect(userDto, validate=True)
    @api.response(201, 'User successfully created')
    @api.doc('Create a new user')
    def post(self):
        """
        Return user created
        """
        data = request.json
        return sv.create(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class UserId(Resource):
    @api.doc('Find user by id')
    @api.marshal_with(userDto)
    def get(self, id):
        """
        Return user by id
        """
        user = sv.findById(id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.expect(userDto, validate=True)
    @api.response(200, 'User successfully edited')
    @api.doc('Edit a user')
    def put(self, id):
        """
        Return user edited
        """
        data = request.json
        return sv.edit(id=id, data=data)

    @api.response(200, 'User successfully removed')
    @api.doc('Remove a user')
    def delete(self, id):
        """
        Return user removed
        """
        return sv.remove(id=id)

@api.route('/find/<username>')
@api.param('username', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('Find user by username')
    @api.marshal_with(userDto)
    def get(self, username):
        """
        Return user by username
        """
        user = sv.findByUserName(username)
        if not user:
            api.abort(404)
        else:
            return user