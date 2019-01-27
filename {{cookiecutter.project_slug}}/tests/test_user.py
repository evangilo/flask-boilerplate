import json
import uuid

import pytest


@pytest.fixture
def app():
    from {{ cookiecutter.project_slug }}.app import app as _app, db

    with _app.app_context():
        db.create_all()

    yield  _app

    db.session.remove()
    db.drop_all()


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def api_request(client):
    def request(method, endpoint, data=None, headers=None):
        if not headers:
            headers = dict()

        headers['Content-Type'] = 'application/json'
        if data:
            data = json.dumps(data)
        requester = getattr(client, method.lower())
        return requester(endpoint, headers=headers, data=data)
    yield request


def test_create_user(api_request):
    resp = api_request('POST', '/api/v1/user', {
        'username': 'test',
        'password': 'test',
        'email': 'test@email.com'
    })
    assert resp.status_code == 201
    assert resp.json == {'message': 'created'}


def test_login(api_request):
    api_request('POST', '/api/v1/user', {
        'username': 'test',
        'password': 'test',
        'email': 'test@email.com'
    })
    resp = api_request('POST', '/api/v1/login', {
        'username': 'test',
        'password': 'test'
    })
    assert resp.status_code == 200
    assert resp.json['access_token'] is not None


def test_user_me(api_request):
    api_request('POST', '/api/v1/user', {
        'username': 'test',
        'password': 'test',
        'email': 'test@email.com'
    })
    resp = api_request('POST', '/api/v1/login', {
        'username': 'test',
        'password': 'test'
    })
    token = resp.json['access_token']
    resp = api_request('GET', '/api/v1/user/me', headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    assert resp.status_code == 200
    assert resp.json == {'username': 'test', 'email': 'test@email.com'}
