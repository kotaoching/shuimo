# -*- coding: utf-8 -*-

from flask import Blueprint
from . import users, topics

bp = Blueprint('api', __name__)


def init_app(app):
    users.api.register(bp)
    topics.api.register(bp)

    app.register_blueprint(bp, url_prefix='/api')