from turtledemo.penrose import inflatedart

from pydantic import BaseModel, Field, model_validator
from bson import ObjectId
import time
from typing import Optional

def get_current_epoch():
    return int(time.time()*1000)

def validate_object_id(data, key, value):
    if isinstance(value, str):
        data[key] = ObjectId(value)
    return value



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

    @model_validator(mode="before")
    def validate_service_data(cls, info):
        user_id = info.get('user_id', None)
        validate_object_id(info, "user_id", user_id)
        return info


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

    @model_validator(mode="before")
    def validate_agent_data(cls, info):
        service_id = info.get('service_id', None)
        validate_object_id(info, "service_id", service_id)
        return info

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

    @model_validator(mode="before")
    def validate_context_data(cls, info):
        context_id = info.get('context_id', None)
        validate_object_id(info,"context_id", context_id)
        return info

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

    @model_validator(mode="before")
    def validate_thread_data(cls, info):
        agent_id = info.get('agent_id', None)
        validate_object_id(info, "agent_id", agent_id)
        context_id = info.get('context_id', None)
        validate_object_id(info, "context_id", context_id)
        return info

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

    @model_validator(mode="before")
    def validate_message_data(cls, info):
        thread_id = info.get('thread_id', None)
        validate_object_id(info, "thread_id", thread_id)
        return info