from flask import Blueprint, request, jsonify
from app.commands import service_commands as service_cmd

service_api = Blueprint("/service", __name__)


@service_api.route('/', methods=["POST"])
def create_service():
    data = request.json
    response = service_cmd.create_service_cmd(data)
    return jsonify(response)

@service_api.route('/<service_id>', methods=["GET"])
def get_service(service_id):
    response = service_cmd.get_service_cmd(service_id)
    return jsonify(response)

@service_api.route('/', methods=["GET"])
def get_all_service():
    response = service_cmd.get_all_service_cmd()
    return jsonify(response)

@service_api.route('/<service_id>', methods=["PUT"])
def update_service(service_id):
    data = request.json
    response = service_cmd.update_service_cmd(service_id, data)
    return jsonify(response)

@service_api.route('/<service_id>', methods=["DELETE"])
def delete_service(service_id):
    response = service_cmd.delete_service_cmd(service_id)
    return jsonify(response)
