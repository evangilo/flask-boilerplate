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


def identity(payload):
    from {{ cookiecutter.project_slug }}.models.core import User
    return User.query.get(payload['identity'])
