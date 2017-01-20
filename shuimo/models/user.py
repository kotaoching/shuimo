# -*- coding: utf-8 -*-

import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .base import db, BaseModel

__all__ = ('User')


class User(BaseModel):
    __tablename__ = 'users'

    ROLE_SUPER = 9
    ROLE_ADMIN = 8
    ROLE_STAFF = 1
    ROLE_UNVERIFIED = 0
    ROLE_SPAMMER = -9

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    description = db.Column(db.String(256))
    location = db.Column(db.String(256))
    website = db.Column(db.String(256))

    role = db.Column(db.SmallInteger, default=0)

    is_delete = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def keys(self):
        return (
            'id', 'username', 'description',
            'created_at', 'updated_at'
        )

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
