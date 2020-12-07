from datetime import datetime
from flask import current_app, request
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    #password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Achievement', backref='author', lazy='dynamic')
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.name

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Achievement(db.Model):
    __tablename__ = 'achievement'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    achievement = db.Column(db.String(150), nullable=False)
    progress = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    isComplete = db.Column(db.Boolean(), unique=False, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Achievement %r>' % self.id   

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
    # blueprint for auth routes in our app