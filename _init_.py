"""_init_.py is used to define app and all blueprints"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)