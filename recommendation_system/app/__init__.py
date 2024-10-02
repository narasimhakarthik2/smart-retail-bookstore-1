from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import recommendations_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(recommendations_bp)

    return app