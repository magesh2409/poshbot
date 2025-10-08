from app.api.service_api import service_api
from app.api.query_api import query_api

def register_blueprints(app):
    app.register_blueprint(service_api, url_prefix='/api/service')
    app.register_blueprint(query_api, url_prefix='/api/query')

