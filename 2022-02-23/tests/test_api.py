from app import db, User


def test_user_info(client):
    response = client.get('/api/user/info')
    assert response.json == {}


def test_login(client):
    db.session.add(User(name='user1'))
    db.session.commit()
    response = client.post('/api/login', json={
        'id': '1'})
    assert response.json['id'] == 1


def test_after_login(client):
    response = client.post('/api/login', json={
        'id': 1})
    response = client.get('/api/user/info')
    assert response.json['id'] == 1
