from models import Thread
from flask import g
from utils import ensure_object_id, default_openai_params
from app.commands.service_commands import create_service_if_not_exists_cmd
from app.commands.agent_commands import create_agent_if_not_exists_cmd
from app.commands.topic_commands import create_topic_if_not_exists_cmd
from app.commands.context_commands import create_context_cmd
from app.commands.context_data_commands import create_context_data_by_listings_info

def create_thread_cmd(data):
    thread = Thread.model_validate(data)
    thread = g.db.thread.insert_one(thread.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(thread.inserted_id), "msg": "thread create successfully" }

def get_thread_cmd(thread_id):
    thread_id = ensure_object_id(thread_id)
    thread = g.db.thread.find_one({"_id":thread_id})
    return thread

def get_all_thread_cmd():
    threads = g.db.thread.find({})
    return threads

def update_thread_cmd(thread_id, data):
    thread_id = ensure_object_id(thread_id)
    thread = g.db.thread.find_one({"_id":thread_id})
    if thread:
        g.db.thread.update_one({"_id":thread_id},{"$set":data})
        return {"msg":"thread updated successfully"}
    return {"msg":"thread not found"}

def delete_thread_cmd(thread_id):
    thread_id = ensure_object_id(thread_id)
    thread = g.db.thread.find_one({"_id":thread_id})
    if thread:
        g.db.thread.delete_one({"_id":thread_id})
        return {"msg":"thread deleted successfully"}
    return {"msg":"thread not found"}

def create_thread_full_api(data):
    data = set_default_openai_params(data)
    service = create_service_if_not_exists_cmd({ "user_id": data["user_id"], "service_name": data["service_name"] })
    agent = create_agent_if_not_exists_cmd({ "service_id": service.get("id"), "model_name": data["model_name"] })
    topic = create_topic_if_not_exists_cmd({ "agent_id": agent.get("id"), "topic_name": data["topic_name"], "model_type": data["model_type"] })
    context = create_context_cmd({})

    listings_info = data["listings_info"]
    context_datas = create_context_data_by_listings_info(listings_info, { "service_id": service.get("id"), "context_id": context.get("id") })
    thread = create_thread_cmd({ "topic_id":topic.get("id"), "context_id": context.get("id") })
    return thread

def set_default_openai_params(data):
    openai_params = default_openai_params()
    openai_params.update(data)
    return openai_params

