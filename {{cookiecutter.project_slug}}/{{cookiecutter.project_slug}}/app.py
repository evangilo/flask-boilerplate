import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from {{ cookiecutter.project_slug }} import auth


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from {{ cookiecutter.project_slug }}.api import *

if __name__ == '__main__':
    app.run()
