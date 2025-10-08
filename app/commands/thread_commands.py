from models import Thread
from flask import g, jsonify
from utils import ensure_object_id

def create_thread_cmd(data):
    thread = Thread.model_validate(data)
    thread = g.db.thread.insert_one(thread.model_dump(exclude_none=True))
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
