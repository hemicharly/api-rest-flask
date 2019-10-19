import unittest
from Base import BaseTestCase
from app.main.service.UserService import UserService

sv = UserService()

class TestUserModel(BaseTestCase):

    def test_findAll(self):
        users = sv.findAll()
        print('users: {0}'.format(users))
        self.assertTrue(users)

    def test_create(self):
        user = {
                "username": "jose",
                "password": "4321",
                "public_id": "1",
                "email": "jose@gmail.com"
            }
        response = sv.create(user)
        print('response: {0}'.format(response))
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()

