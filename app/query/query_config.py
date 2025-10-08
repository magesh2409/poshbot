from flask import g
from utils import ensure_object_id
from types import SimpleNamespace

class QueryConfig:
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.service = None
        self.agent = None
        self.context = None
        self.topic = None
        self.context_data = None
        self.thread = None
        self.populate_config()

    def populate_config(self):
        db = g.db
        self.thread = db.thread.find_one({ "_id": ensure_object_id(self.thread_id) })
        topic_id = self.thread.get("topic_id", None)
        context_id = self.thread.get("context_id", None)

        self.topic = db.topic.find_one({ "_id": ensure_object_id(topic_id)}) if topic_id else None
        self.context = db.context.find_one({ "_id": context_id}) if context_id else None

        agent_id = self.topic.get("agent_id", None) if self.topic else None
        self.agent = db.agent.find_one({ "_id": ensure_object_id(agent_id)}) if agent_id else None

        if self.context:
            self.context_data = db.context_data.find({ "context_id": ensure_object_id(context_id) })

        service_id = self.agent.get("service_id", None)
        self.service = db.service.find_one({ "_id": ensure_object_id(service_id) })

        #convert to simple namespace
        self.service = SimpleNamespace(**self.service) if self.service else None
        self.agent = SimpleNamespace(**self.agent) if self.agent else None
        self.topic = SimpleNamespace(**self.topic) if self.topic else None
        self.context = SimpleNamespace(**self.context) if self.context else None
        self.thread = SimpleNamespace(**self.thread)  if self.thread else None
        return
