from flask import Flask, current_app, jsonify, g
from db.db import initialize_db, get_db
from bson import ObjectId


def create_app():
    app = Flask(__name__)
    initialize_db(app)


    @app.route('/')
    def home():
        return { "message": "Welcome to POSHMARK AI Service" }

    @app.route('/health')
    def health():
        return { "message": "POSHMARK AI Service is health" }

    @app.before_request
    def before_request():
        db = get_db()

    # @app.route('/agent')
    # def agent():
    #     db = g.db
    #     db.service.insert_one({ "user_id": ObjectId(), "service_name": "Openai"})
    #     db.agent.insert_one({ "user_id": ObjectId(), "service_id": ObjectId()})
    #     response = db.service.find({})
    #     return jsonify(response).data
    return app



