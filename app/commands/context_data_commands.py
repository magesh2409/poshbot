from models import ContextData
from flask import g, jsonify
from utils import ensure_object_id
from app.commands.openai_utils import handle_listing_file

def create_context_data_cmd(data):
    handle_listing_file(data)
    context_data = ContextData.model_validate(data)
    context_data = g.db.context_data.insert_one(context_data.model_dump(exclude_none=True, by_alias=True))
    return { "id": str(context_data.inserted_id), "msg": "context data create successfully" }

def get_context_data_cmd(context_data_id):
    context_data_id = ensure_object_id(context_data_id)
    context_data = g.db.context_data.find_one({"_id":context_data_id})
    return context_data

def get_all_context_data_cmd():
    context_data = g.db.context_data.find({})
    return context_data

def update_context_data_cmd(context_data_id, data):
    context_data_id = ensure_object_id(context_data_id)
    context_data = g.db.context_data.find_one({"_id":context_data_id})
    if context_data:
        g.db.context_data.update_one({"_id":context_data_id},{"$set":data})
        return {"msg":"context data updated successfully"}
    return {"msg":"context data not found"}

def delete_context_data_cmd(context_data_id):
    context_data_id = ensure_object_id(context_data_id)
    context_data = g.db.context_data.find_one({"_id":context_data_id})
    if context_data:
        g.db.context_data.delete_one({"_id":context_data_id})
        return {"msg":"context data deleted successfully"}
    return {"msg":"context data not found"}

def create_context_data_by_listings_info(listings_info, data):
    create_meta_content_payload(listings_info, data)
    cover_shot = listings_info.get("cover_shot", None)
    if cover_shot:
        url = cover_shot.get("url", None)
        if url:
            payload = {
                "service_id" : data["service_id"],
                "context_id" : data["context_id"],
                "s3_url" : url
            }
            create_context_data_cmd(payload)

    pictures_list = listings_info.get("pictures", [])
    for picture in pictures_list:
        url = picture.get("url", None)
        if url:
            payload = {
                "service_id" : data["service_id"],
                "context_id" : data["context_id"],
                "s3_url" : url
            }
            create_context_data_cmd(payload)

def create_meta_content_payload(listings_info, data):
    payload = {
        "service_id": data["service_id"],
        "context_id": data["context_id"],
        "meta_content": str(listings_info)
    }
    create_context_data_cmd(payload)