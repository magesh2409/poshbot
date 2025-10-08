from flask import Blueprint, request, jsonify
from app.commands import thread_commands as thread_cmd

thread_api = Blueprint("thread", __name__)

@thread_api.route("/", methods=["POST"])
def create_thread():
    data = request.json
    response = thread_cmd.create_thread_cmd(data)
    return jsonify(response)

@thread_api.route("/<thread_id>", methods=["GET"])
def get_thread(thread_id):
    response = thread_cmd.get_thread_cmd(thread_id)
    return jsonify(response)

@thread_api.route("/", methods=["GET"])
def get_all_thread():
    response = thread_cmd.get_all_thread_cmd()
    return jsonify(response)

@thread_api.route("/<thread_id>", methods=["PUT"])
def update_thread(thread_id):
    data = request.json
    response = thread_cmd.update_thread_cmd(thread_id, data)
    return jsonify(response)

@thread_api.route("/<thread_id>", methods=["DELETE"])
def delete_thread(thread_id):
    response = thread_cmd.delete_thread_cmd(thread_id)
    return jsonify(response)
