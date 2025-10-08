
from utils import read_db_config
from flask_pymongo import PyMongo
from flask import current_app, g
import certifi


def initialize_db(app):
    db_config = read_db_config()
    mongo_uri = db_config['MONGO_URI'] + '/' + db_config["DB_NAME"]
    app.config['MONGO_URI'] = mongo_uri
    mongo = PyMongo(app, tlsCAFile=certifi.where())
    app.mongo = mongo

    app.logger.info("Setted up Mongo")
    # return mongo

def get_db():
    if "db" not in g:
        g.db = current_app.mongo.db
    return g.db
