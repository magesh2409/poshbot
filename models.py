from pydantic import BaseModel, Field
from bson import ObjectId
import time
from typing import Optional

def get_current_epoch():
    return int(time.time()*1000)



class Service(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: ObjectId = Field(alias="user_id")
    service_name: str = Field(max_length=50)
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }

data = {
    "service_name" : "google",
    "user_id" : ObjectId(),
    "a" : "b"
}

service = Service.model_validate(data)
print(service)
class Agent(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    service_id: ObjectId = Field(alias="service_id")
    model_name: str = Field(max_length=50)
    hyper_params: Optional[dict]
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }

class Context(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }

class ContextData(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    context_id: ObjectId
    s3_url: Optional[str] = Field(max_length=100)
    file_id: Optional[str] = Field(max_length=100)
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }

class Thread(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    agent_id: ObjectId
    context_id: ObjectId
    thread_meta: Optional[dict]
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }

class Message(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    thread_id: ObjectId
    response: str
    created_at: int = Field(default_factory=get_current_epoch)
    updated_at: int = Field(default_factory=get_current_epoch)

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "json_encoders": {ObjectId: str},
        "extra": "forbid"
    }