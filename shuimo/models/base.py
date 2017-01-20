# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        data = {}
        for key in self.keys():
            data[key] = str(getattr(self, key))

        return data