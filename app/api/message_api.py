from flask import Blueprint, request, jsonify
from app.commands import message_commands as message_cmd

message_api = Blueprint("message", __name__)

@message_api.route('/', methods=["POST"])
def create_message():
    data = request.json
    response = message_cmd.create_message_cmd(data)
    return jsonify(response)

@message_api.route('/<message_id>',methods=["GET"])
def get_message(message_id):
    response = message_cmd.get_message_cmd(message_id)
    return jsonify(response)

@message_api.route('/',methods=["GET"])
def get_all_message():
    response = message_cmd.get_all_message_cmd()
    return jsonify(response)

@message_api.route('/<message_id>',methods=["PUT"])
def update_message(message_id):
    data = request.json
    response = message_cmd.update_message_cmd(message_id,data)
    return jsonify(response)

@message_api.route('/<message_id>',methods=["DELETE"])
def delete_message():
    data = request.json
    response = message_cmd.delete_message_cmd(data)
    return jsonify(response)
