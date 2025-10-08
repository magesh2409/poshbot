from flask import g, jsonify
from app.query.query_config import QueryConfig
from app.services.service_maps import service_map

def run_query_cmd(thread_id, data):
    query_config = QueryConfig(thread_id)
    service_name = query_config.service.service_name

    service_class = service_map.get(service_name, None)
    service = service_class(query_config)

    model_type = query_config.topic.model_type
    method = getattr(service, model_type, "chat_completion")

    response = method(data["message"])
    return jsonify({"response": response})