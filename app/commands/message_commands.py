from models import Service
from flask import g, jsonify
from utils import ensure_object_id


def create_message_cmd(data):
    message = Service.model_validate(data)
    message = g.db.service.insert_one(message.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(message.inserted_id), "msg": "service create successfully" }

def get_message_cmd(message_id):
    message_id = ensure_object_id(message_id)
    message = g.db.service.find_one({"_id":message_id})
    return message

def get_all_message_cmd():
    messages = g.db.service.find({})
    return messages

def update_message_cmd(message_id, data):
    message_id = ensure_object_id(message_id)
    message = g.db.service.find_one({"_id":message_id})
    if message:
        g.db.service.update_one({"_id":message_id},{"$set":data})
        return {"msg":"service updated successfully"}
    return {"msg":"service not found"}

def delete_message_cmd(message_id):
    message_id = ensure_object_id(message_id)
    message = g.db.service.find_one({"_id":message_id})
    if message:
        g.db.service.delete_one({"_id":message_id})
        return {"msg":"service deleted successfully"}
    return {"msg":"service not found"}
