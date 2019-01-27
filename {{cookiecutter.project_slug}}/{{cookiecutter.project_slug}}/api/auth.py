# -*- coding: utf-8 -*-
from flask import request, jsonify

from {{ cookiecutter.project_slug }} import auth
from {{ cookiecutter.project_slug }}.app import db, app


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify(message='Missing username'), 400
    if not password:
        return jsonify(message='Missing password'), 400

    user = auth.authenticate(username, password)
    if not user:
        return jsonify(message='Bad username or password'), 401

    return jsonify(access_token=auth.create_token(user)), 200
