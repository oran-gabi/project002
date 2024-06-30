# backend/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load environment variables from backend/.env/my.md
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env', 'my.md')
    load_dotenv(dotenv_path)

    # Load configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Import and register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
