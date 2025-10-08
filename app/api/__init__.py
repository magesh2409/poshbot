from app.api.service_api import service_api
from app.api.agent_api import agent_api
from app.api.thread_api import thread_api
from app.api.message_api import message_api
from app.api.context_api import context_api
from app.api.context_data_api import context_data_api
from app.api.topic_api import topic_api
def register_blueprints(app):
    app.register_blueprint(service_api, url_prefix='/api/service')
    app.register_blueprint(agent_api, url_prefix='/api/agent')
    app.register_blueprint(context_api, url_prefix='/api/context')
    app.register_blueprint(context_data_api, url_prefix='/api/context_data')
    app.register_blueprint(message_api, url_prefix='/api/message')
    app.register_blueprint(topic_api, url_prefix='/api/topic')
    app.register_blueprint(thread_api, url_prefix='/api/thread')

