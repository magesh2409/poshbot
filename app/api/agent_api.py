from flask import Blueprint, request, jsonify
from app.commands import agent_commands as agent_cmd


agent_api = Blueprint("agent", __name__)


@agent_api.route("/", methods=["POST"])
def create_agent():
    data = request.json
    response = agent_cmd.create_agent_cmd(data)
    return jsonify(response)

@agent_api.route("/<agent_id>", methods=["GET"])
def get_agent(agent_id):
    response = agent_cmd.get_agent_cmd(agent_id)
    return jsonify(response)

@agent_api.route("/", methods=["GET"])
def get_all_agent():
    response = agent_cmd.get_all_agent_cmd()
    return jsonify(response)

@agent_api.route("/<agent_id>", methods=["PUT"])
def update_agent(agent_id):
    data = request.json
    response = agent_cmd.update_agent_cmd(agent_id, data)
    return jsonify(response)

@agent_api.route("/<agent_id>", methods=["DELETE"])
def delete_agent(agent_id):
    response = agent_cmd.delete_agent_cmd(agent_id)
    return jsonify(response)
