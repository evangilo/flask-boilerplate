# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask_jwt import jwt_required, current_identity

from {{ cookiecutter.project_slug }}.app import db, app
from {{ cookiecutter.project_slug }}.auth import gen_password_hash
from {{ cookiecutter.project_slug }}.models import core


@app.route('/api/v1/user/me', methods=['GET'])
@jwt_required()
def user_me():
    user = current_identity
    return jsonify({
        'username': user.username,
        'email': user.email
    })


@app.route('/api/v1/user', methods=['POST'])
def user_create():
    data = request.json
    username = data['username']
    email = data['email']
    password = gen_password_hash(data['password'])

    db.session.add(core.User(
        username=username,
        email=email,
        password=password,
    ))
    db.session.commit()

    return jsonify({'message': 'created'}), 201
