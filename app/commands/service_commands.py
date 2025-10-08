from models import Service
from flask import g, jsonify
from utils import ensure_object_id

def create_service_cmd(data):
    service = Service.model_validate(data)
    service = g.db.service.insert_one(service.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(service.inserted_id), "msg": "service create successfully" }

def get_service_cmd(service_id):
    service_id = ensure_object_id(service_id)
    service = g.db.service.find_one({ "_id": service_id })
    return service

def get_all_service_cmd():
    services = g.db.service.find({})
    return services

def update_service_cmd(service_id, data):
    service_id = ensure_object_id(service_id)
    service = g.db.service.find_one({ "_id": service_id })
    if service:
        g.db.service.update_one({ "_id": service_id }, { "$set": data })
        return { "msg": "service updated successfully" }
    return { "msg": "service not found" }

def delete_service_cmd(service_id):
    service_id = ensure_object_id(service_id)
    service = g.db.service.find_one({ "_id": service_id })
    if service:
        g.db.service.delete_one({ "_id": service_id })
        return { "msg": "service deleted successfully" }
    return { "msg": "service not found" }