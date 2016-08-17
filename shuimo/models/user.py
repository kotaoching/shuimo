# -*- coding: utf-8 -*-

import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ._base import db

__all__ = ('User')


class User(db.Model):
    __tablename__ = 'users'

    ROLE_SUPER = 9
    ROLE_ADMIN = 8
    ROLE_STAFF = 7
    ROLE_VERIFIED = 3
    ROLE_ACTIVE = 1
    ROLE_SPAMMER = -9

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    email = db.Column(db.String(200), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(255))
    location = db.Column(db.String(255))
    website = db.Column(db.String(200))

    role = db.Column(db.SmallInteger, default=0)
    deleted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)
