# -*- coding: utf-8 -*-

import datetime
from .base import db, BaseModel


class Resource(BaseModel):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    format = db.Column(db.Text)

    author_id = db.Column(db.Integer, nullable=False, index=True)

    type = db.Column(db.String(100), nullable=False)
    privilege = db.Column(db.String(100), nullable=False)

    deleted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
