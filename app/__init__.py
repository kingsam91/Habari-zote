from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from app import error
# from flask import Blueprint

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing Flask Extensions
    Bootstrap(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)



    return app
