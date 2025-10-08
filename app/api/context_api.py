from http.client import responses
from flask import Blueprint, request, jsonify
from app.commands import context_commands as context_cmd

context_api = Blueprint("context", __name__)

@context_api.route("/", methods=["POST"])
def create_context():
    data = request.json
    response = context_cmd.create_context_cmd(data)
    return jsonify(response)

@context_api.route("/<context_id>", methods=["GET"])
def get_context(context_id):
    response = context_cmd.get_context_cmd(context_id)
    return jsonify(response)

@context_api.route("/", methods=["GET"])
def get_all_context():
    response = context_cmd.get_all_context_cmd()
    return jsonify(response)

@context_api.route("/<context_id>", methods=["PUT"])
def update_context(context_id):
    data = request.json
    response = context_cmd.update_context_cmd(context_id, data)
    return jsonify(response)

@context_api.route("/<context_id>", methods=["DELETE"])
def delete_context(context_id):
    response = context_cmd.delete_context_cmd(context_id)
    return jsonify(response)
