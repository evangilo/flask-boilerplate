import datetime
import os


basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# https://flask-jwt-extended.readthedocs.io/en/latest/options.html
JWT_SECRET_KEY = 'super-secret'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=31)
