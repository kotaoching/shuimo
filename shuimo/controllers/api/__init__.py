# -*- coding: utf-8 -*-

from flask import Blueprint
from . import users, resources

bp = Blueprint('api', __name__)


def init_api(app):
    users.api.register(bp)
    resources.api.register(bp)

    app.register_blueprint(bp, url_prefix='/api')