from flask import Flask, jsonify, request
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_login import LoginManager, current_user, UserMixin, login_user

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'secret_key',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///comment.db'
})


db = SQLAlchemy(app)
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)


@app.route('/api/login', methods=['post'])
def login():
    user = User.query.get(request.json['id'])

    login_user(user)
    return jsonify({'id': user.id})


@app.route('/api/user/info')
def user_info():
    if current_user.is_anonymous:
        return {}
    return {
        'id': current_user.id
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=app.debug, threaded=True)
