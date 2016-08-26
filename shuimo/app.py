# -*- coding: utf-8 -*-

import time
from flask import Flask
from flask import request, g


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    register_base(app)
    register_database(app)
    register_blueprint(app)
    register_hooks(app)

    return app


def register_base(app):
    # app.session_interface = RedisSessionInterface()
    return None


def register_database(app):
    from shuimo.models import db
    db.init_app(app)


def register_blueprint(app):
    from shuimo.controllers.api import init_app
    init_app(app)

    from shuimo.controllers import account

    app.register_blueprint(account.bp, url_prefix='/account')


def register_hooks(app):
    """Hooks for request."""
    from .utils.account import get_current_user

    @app.before_request
    def load_current_user():
        g.user = get_current_user()
        if g.user:
            g._before_request_time = time.time()

    @app.after_request
    def rendering_time(response):
        if hasattr(g, '_before_request_time'):
            delta = time.time() - g._before_request_time
            response.headers['X-Render-Time'] = delta * 1000
        return response