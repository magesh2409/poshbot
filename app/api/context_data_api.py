from flask import Blueprint, request, jsonify
from app.commands import context_data_commands as context_data_cmd

context_data_api = Blueprint("context_data", __name__)

@context_data_api.route("/", methods=["POST"])
def create_context_data():
    data = request.json
    response = context_data_cmd.create_context_data_cmd(data)
    return jsonify(response)

@context_data_api.route("/<context_data_id>", methods=["GET"])
def get_context_data(context_data_id):
    response = context_data_cmd.get_context_data_cmd(context_data_id)
    return jsonify(response)

@context_data_api.route("/", methods=["GET"])
def get_all_context_data():
    response = context_data_cmd.get_all_context_data_cmd()
    return jsonify(response)

@context_data_api.route("/<context_data_id>", methods=["PUT"])
def update_context_data(context_data_id):
    data = request.json
    response = context_data_cmd.update_context_data_cmd(context_data_id, data)
    return jsonify(response)

@context_data_api.route("/<context_data_id>", methods=["DELETE"])
def delete_context_data(context_data_id):
    response = context_data_cmd.delete_context_data_cmd(context_data_id)
    return jsonify(response)

