from http.client import responses

from flask import Blueprint, request, jsonify

from app.api import service_api
from app.commands import topic_commands as topic_cmd

topic_api = Blueprint("topic", __name__)

@topic_api.route("/", methods=["POST"])
def create_topic():
    data = request.json
    response = topic_cmd.create_topic_cmd(data)
    return jsonify(response)

@topic_api.route("/<topic_id>", methods=["GET"])
def get_service(topic_id):
    response = topic_cmd.get_topic_cmd(topic_id)
    return jsonify(response)

@topic_api.route("/", methods=["GET"])
def get_all_topic():
    response = topic_cmd.get_all_topic_cmd()
    return jsonify(response)

@topic_api.route("/<topic_id>", methods=["PUT"])
def update_service(topic_id):
    data = request.json
    response = topic_cmd.update_topic_cmd(topic_id, data)
    return jsonify(response)

@topic_api.route("/<topic_id>", methods=["DELETE"])
def delete_service(topic_id):
    response = topic_cmd.delete_topic_cmd(topic_id)
    return jsonify(response)