import datetime
import os


basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
# JWT: https://pythonhosted.org/Flask-JWT/#configuration-options
JWT_AUTH_URL_RULE = '/api/v1/auth'
JWT_SECRET_KEY = 'super-secret'
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_DELTA = datetime.timedelta(days=31)
