import yaml
from bson import ObjectId

def read_db_config():
    with open("db/db_config.yml", "r") as file:
        return yaml.safe_load(file)

def ensure_object_id(id):
    if isinstance(id, str):
        return ObjectId(id)
    return id

def read_mcp_config():
    with open("conf/mcp_conf.yml", "r") as file:
        return yaml.safe_load(file)
