"""Initialize Flask app."""
from flask import Flask
from flask_cors import CORS
from backend_main import init_routes

cors = CORS()


def init_app():
    """Construct core Flask application."""
    # app = Flask(__name__, instance_relative_config=False)
    app = Flask(__name__)
    # app.config.from_object('config.ApplicationConfig')

    # Initialize Plugins

    cors.init_app(app)

    # Initialize routes

    with app.app_context():
        app = init_routes(app)

    return app