from .api import blueprint
from .db import CustomerRequests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from x_x import x_x


def get_app(debug=False):

    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "WHATEVER"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["TESTING"] = True
    app.jinja_env.globals["x_x"] = x_x

    db = SQLAlchemy()

    db.init_app(app)

    if debug:
        app.config["SQLALCHEMY_ECHO"] = True
        logger = app.logger
        logger.setLevel("DEBUG")

    # ...
    app.register_blueprint(blueprint())

    return app
