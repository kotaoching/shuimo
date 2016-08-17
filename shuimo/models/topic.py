# -*- coding: utf-8 -*-

import datetime
from ._base import db


class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)

    author_id = db.Column(db.Integer, nullable=False, index=True)
    tag_id = db.Column(db.Integer, nullable=False, index=True)

    opinion_count = db.Column(db.Integer, default=0)
    comment_count = db.Column(db.Integer, default=0)
    contributor_count = db.Column(db.Integer, default=0)

    deleted = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<User %r>' % self.username