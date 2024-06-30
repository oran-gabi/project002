from flask import Flask
from flask_cors import CORS
from .extensions import db
from app.routes import api


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

  
    app.register_blueprint(api, url_prefix='/api')
    

    with app.app_context():
        db.create_all()

    return app
