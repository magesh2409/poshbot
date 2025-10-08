from models import Context
from flask import g, jsonify
from utils import ensure_object_id

def create_context_cmd(data):
    context = Context.model_validate(data)
    context = g.db.context.insert_one(context.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(context.inserted_id), "msg": "context create successfully" }

def get_context_cmd(context_id):
    context_id = ensure_object_id(context_id)
    context = g.db.context.find_one({"_id":context_id})
    return context

def get_all_context_cmd():
    contexts = g.db.context.find({})
    return contexts

def update_context_cmd(context_id, data):
    context_id = ensure_object_id(context_id)
    context = g.db.context.find_one({"_id":context_id})
    if context:
        g.db.context.update_one({"_id":context_id},{"$set":data})
        return {"msg":"context updated successfully"}
    return {"msg":"context not found"}

def delete_context_cmd(context_id):
    context_id = ensure_object_id(context_id)
    context = g.db.context.find_one({"_id":context_id})
    if context:
        g.db.context.delete_one({"_id":context_id})
        return {"msg":"context deleted successfully"}
    return {"msg":"context not found"}
