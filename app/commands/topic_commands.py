from models import Topic
from flask import g, jsonify
from utils import ensure_object_id

def create_topic_cmd(data):
    topic = Topic.model_validate(data)
    topic = g.db.topic.insert_one(topic.model_dump(exclude_none=True))
    return { "id": str(topic.inserted_id), "msg": "topic create successfully" }

def get_topic_cmd(topic_id):
    topic_id = ensure_object_id(topic_id)
    topic = g.db.topic.find_one({"_id":topic_id})
    return topic

def get_all_topic_cmd():
    topics = g.db.topic.find({})
    return topics

def update_topic_cmd(topic_id, data):
    topic_id = ensure_object_id(topic_id)
    topic = g.db.topic.find_one({"_id":topic_id})
    if topic:
        g.db.topic.update_one({"_id":topic_id},{"$set":data})
        return {"msg":"topic updated successfully"}
    return {"msg":"topic not found"}

def delete_topic_cmd(topic_id):
    topic_id = ensure_object_id(topic_id)
    topic = g.db.topic.find_one({"_id":topic_id})
    if topic:
        g.db.topic.delete_one({"_id":topic_id})
        return {"msg":"topic deleted successfully"}
    return {"msg":"topic not found"}