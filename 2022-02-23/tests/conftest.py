import os

import pytest

from app import app as _app, db


@pytest.fixture(scope='session')
#@pytest.fixture
def app():
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    with _app.app_context():
        db.create_all()
    yield _app

    os.remove('test.db')


@pytest.fixture
def client(app):
    return app.test_client()
