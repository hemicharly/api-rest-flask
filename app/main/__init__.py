from flask import Flask

from ..main.configure.Config import configByName

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configByName[config_name])
    return app