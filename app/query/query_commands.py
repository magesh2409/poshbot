from flask import g, jsonify
from app.query.query_config import QueryConfig
from app.services.service_maps import service_map
from app.commands.message_commands import create_message_cmd
from app.commands.thread_commands import update_thread_cmd
import time

def run_query_cmd(thread_id, data):
    query_config = QueryConfig(thread_id)
    service_name = query_config.service.service_name

    service_class = service_map.get(service_name, None)
    service = service_class(query_config)

    model_type = query_config.topic.model_type
    create_message_cmd({ "thread_id": thread_id, "role": "user", "message": data["message"]})
    method = getattr(service, model_type, "chat_completion")

    response = method(data["message"])
    response = post_response_cmd(thread_id, response)
    return jsonify(response)

def post_response_cmd(thread_id, response):
    if "thread_meta" in response:
        update_thread_cmd(thread_id, { "thread_meta": response["thread_meta"], "updated_at": int(time.time()*1000)})
    create_message_cmd({ "thread_id": thread_id, "role": "system", "message": response["message"]})
    return response