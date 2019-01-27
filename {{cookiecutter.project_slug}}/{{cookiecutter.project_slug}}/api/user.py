# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask_jwt_extended import jwt_required

from {{ cookiecutter.project_slug }} import auth
from {{ cookiecutter.project_slug }}.app import db, app
from {{ cookiecutter.project_slug }}.models import core


@app.route('/api/v1/user/me', methods=['GET'])
@jwt_required
def user_me():
    user = auth.get_logged_user()
    return jsonify({
        'username': user.username,
        'email': user.email
    })


@app.route('/api/v1/user', methods=['POST'])
def user_create():
    data = request.json
    username = data['username']
    email = data['email']
    password = auth.gen_password_hash(data['password'])

    db.session.add(core.User(
        username=username,
        email=email,
        password=password,
    ))
    db.session.commit()

    return jsonify({'message': 'created'}), 201
