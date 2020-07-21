from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from . import error
# from flask import Blueprint

def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    Bootstrap(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
