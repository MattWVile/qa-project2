from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
from . import routes
import requests

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db",
    SQLALCHEMY_TRACK_MODIFICATINOS=True,
    SECRET_KEY=str(os.urandom(16))
)

db = SQLAlchemy(app)


api = 'http://localhost:5000'