from flask_api import FlaskAPI
from flask_pymongo import MongoClient
from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    mongo = MongoClient('localhost', 27017)
    db = mongo['erpsy']

    @app.route('/parts/', methods=['GET'])
    def parts():
        parts = db['parts'].find()
        return [{'part_number': p['part_number'], 'name': p['part_name'], 'description':p['description']} for p in parts]
    return app
