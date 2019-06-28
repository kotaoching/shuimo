# -*- coding: utf-8 -*-

from flask import Blueprint
from . import user

bp = Blueprint('admin', __name__)


def init_admin(app):
    user.admin.register(bp)

    app.register_blueprint(bp, url_prefix='/admin')