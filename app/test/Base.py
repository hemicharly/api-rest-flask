from flask_testing import TestCase

from manage import app

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.configure.Config.TestingConfig')
        return app