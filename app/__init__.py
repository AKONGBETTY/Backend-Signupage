from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()


jwt = JWTManager()
mongo = PyMongo()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    flask_app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    mongo.init_app(flask_app)
    jwt.init_app(flask_app)

    try:
        mongo.db.command('ping')
        print("Connected to MongoDB!")
    except Exception as e:
        print("Error connecting to MongoDB:", e)

    @flask_app.route('/')
    def home():
        return "Hello, Flag!"

    from .auth import auth_bp as auth_blueprint
    flask_app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return flask_app
