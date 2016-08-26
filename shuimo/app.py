# -*- coding: utf-8 -*-

from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    register_base(app)
    register_blueprint(app)

    return app


def register_base(app):
    from shuimo.models import db
    db.init_app(app)

    # app.session_interface = RedisSessionInterface()

    # with app.app_context():
    #     db.create_all()


def register_blueprint(app):
    from shuimo.controllers.api import init_app
    init_app(app)

    from shuimo.controllers import account

    app.register_blueprint(account.bp, url_prefix='/account')