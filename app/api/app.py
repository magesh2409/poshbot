from flask import Flask
from db.db import initialize_db, get_db
from app.api import register_blueprints


def create_app():
    app = Flask(__name__)
    initialize_db(app)
    register_blueprints(app)

    @app.route('/')
    def home():
        return { "message": "Welcome to POSHMARK AI Service" }

    @app.route('/health')
    def health():
        return { "message": "POSHMARK AI Service is health" }

    @app.before_request
    def before_request():
        db = get_db()

    return app



