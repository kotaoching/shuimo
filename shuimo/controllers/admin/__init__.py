# -*- coding: utf-8 -*-

from flask import Blueprint
from . import users

bp = Blueprint('admin', __name__)


def init_admin(app):
    users.admin.register(bp)

    app.register_blueprint(bp, url_prefix='/admin')