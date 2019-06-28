# -*- coding: utf-8 -*-

from flask import Blueprint
from . import user, painting

bp = Blueprint('api', __name__)


def init_api(app):
    user.api.register(bp)
    painting.api.register(bp)

    app.register_blueprint(bp, url_prefix='/api')