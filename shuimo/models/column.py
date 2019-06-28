# -*- coding: utf-8 -*-

import datetime
from .base import db, BaseModel


class Column(BaseModel):
    __tablename__ = 'columns'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(256))

    user_id = db.Column(db.Integer, nullable=False, index=True)

    article_count = db.Column(db.Integer, nullable=False)

    is_deleted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
