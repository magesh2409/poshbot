from models import Agent
from flask import g, jsonify
from utils import ensure_object_id

def create_agent_cmd(data):
    agent = Agent.model_validate(data)
    agent = g.db.agent.insert_one(agent.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(agent.inserted_id), "msg": "agent create successfully" }

def get_agent_cmd(agent_id):
    agent_id = ensure_object_id(agent_id)
    agent = g.db.agent.find_one({ "_id": agent_id })
    return agent

def get_all_agent_cmd():
    agents = g.db.agent.find({})
    return agents

def update_agent_cmd(agent_id, data):
    agent_id = ensure_object_id(agent_id)
    agent = g.db.agent.find_one({ "_id": agent_id })
    if agent:
        g.db.agent.update_one({ "_id": agent_id }, { "$set": data })
        return { "msg": "agent updated successfully" }
    return { "msg": "agent not found" }

def delete_agent_cmd(agent_id):
    agent_id = ensure_object_id(agent_id)
    agent = g.db.agent.find_one({ "_id": agent_id })
    if agent:
        g.db.agent.delete_one({ "_id": agent_id })
        return { "msg": "agent deleted successfully" }
    return { "msg": "agent not found" }
