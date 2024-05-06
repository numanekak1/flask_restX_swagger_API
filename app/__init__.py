from flask import Flask

# Local Modules 
from .extensions import api,db 
from .resources import ns

def create_app():
    app = Flask(__name__)  #app_instance

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.sqlite3"

    api.init_app(app) # Rest API
    db.init_app(app) # DB ORM

    api.add_namespace(ns)

    return app