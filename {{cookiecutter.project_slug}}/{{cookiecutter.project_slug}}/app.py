from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_envvar('{{ cookiecutter.project_slug|upper }}_SETTINGS')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from {{ cookiecutter.project_slug }}.api import *
