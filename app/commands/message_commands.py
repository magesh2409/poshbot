from models import Message
from flask import g, jsonify
from utils import ensure_object_id


def create_message_cmd(data):
    message = Message.model_validate(data)
    message = g.db.message.insert_one(message.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(message.inserted_id), "msg": "message create successfully" }

def get_message_cmd(message_id):
    message_id = ensure_object_id(message_id)
    message = g.db.message.find_one({"_id":message_id})
    return message

def get_all_message_cmd():
    messages = g.db.message.find({})
    return messages

def update_message_cmd(message_id, data):
    message_id = ensure_object_id(message_id)
    message = g.db.message.find_one({"_id":message_id})
    if message:
        g.db.message.update_one({"_id":message_id},{"$set":data})
        return {"msg":"message updated successfully"}
    return {"msg":"message not found"}

def delete_message_cmd(message_id):
    message_id = ensure_object_id(message_id)
    message = g.db.message.find_one({"_id":message_id})
    if message:
        g.db.message.delete_one({"_id":message_id})
        return {"msg":"message deleted successfully"}
    return {"msg":"message not found"}
