users = [
    {
        "username": "hemicharly",
        "password": "1234",
        "public_id": "1",
        "email": "hemicharlythiago@gmail.com"
    },
    {
        "username": "thiago",
        "password": "1234",
        "public_id": "1",
        "email": "thiago@gmail.com"
    }
]


class UserService:
    def __init__(self):
        pass

    def create(self, data):
        response = {
            'status': 'success',
            'message': 'User created',
            "data": data
        }
        return response, 201

    def findAll(self):
        response = users
        return response, 200

    def findByUserName(self, username):
        response = {}
        for user in users:
            if user['username'] == username:
                response = user
                break
        return response, 200
