from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    Bootstrap(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(404)
    def _handle_api_error(ex):
        return render_template('errors/404.html')

    return app
