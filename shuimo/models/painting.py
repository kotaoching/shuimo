# -*- coding: utf-8 -*-

import datetime
from .base import db, BaseModel


class Painting(BaseModel):
    __tablename__ = 'paintings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    content = db.Column(db.Text)

    user_id = db.Column(db.Integer, nullable=False, index=True)
    
    comment_count = db.Column(db.Integer, nullable=False)

    type = db.Column(db.String(100), nullable=False)
    privilege = db.Column(db.String(100), nullable=False)

    is_deleted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
