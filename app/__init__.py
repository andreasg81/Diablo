from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
mongo = PyMongo(app)

from app import routes