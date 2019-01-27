# -*- coding: utf-8 -*

def check_password(hashed_password, password):
    from werkzeug.security import check_password_hash
    return check_password_hash(hashed_password, password)


def gen_password_hash(password):
    from werkzeug.security import generate_password_hash
    return generate_password_hash(password)


def authenticate(username, password):
    from {{ cookiecutter.project_slug }}.models.core import User
    user = User.query.filter_by(username=username).first()
    if user and check_password(user.password, password):
        return user
    return None


def create_token(user):
    from flask_jwt_extended import create_access_token
    return create_access_token(identity=user.username)


def get_logged_user():
    from flask_jwt_extended import get_jwt_identity
    from {{ cookiecutter.project_slug }}.models.core import User
    username = get_jwt_identity()
    return username and User.query.filter_by(username=username).first()
