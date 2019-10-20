users = [
    {
        "id": 1,
        "username": "pedro",
        "password": "1234",
        "email": "pedro@gmail.com"
    },
    {
        "id": 2,
        "username": "thiago",
        "password": "1234",
        "email": "thiago@gmail.com"
    },
    {
        "id": 3,
        "username": "joao",
        "password": "1234",
        "email": "joao@gmail.com"
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
        return response

    def edit(self, id, data):
        response = {
            'status': 'success',
            'message': 'User edited',
            "data": self._edit(id, data)
        }
        return response

    def remove(self, id):
        response = {
            'status': 'success',
            'message': 'User removed',
            "data": self.findById(id)
        }
        return response

    def findAll(self):
        response = users
        return response

    def findById(self, id):
        response = {}
        for user in users:
            if user['id'] == int(id):
                response = user
                break
        return response

    def findByUserName(self, username):
        response = {}
        for user in users:
            if user['username'] == str(username):
                response = user
                break
        return response

    def _edit(self, id, data):
        user = self.findById(id)

        if user != {}:
            user['username'] = data['username']
            user['password'] = data['password']
            user['email'] = data['email']

        return user
