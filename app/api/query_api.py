from flask import Blueprint, jsonify, request
from app.query.query_commands import run_query_cmd


query_api = Blueprint("query", __name__)

@query_api.route("/<thread_id>", methods=["POST"])
def query_response(thread_id):
    data = request.json
    return run_query_cmd(thread_id, data)






