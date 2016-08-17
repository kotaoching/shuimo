# -*- coding: utf-8 -*-

from flask_script import Manager
from shuimo import create_app
from shuimo.models import db, User

app = create_app()
manager = Manager(app)


@manager.command
def createdb():
    """Creates the db tables."""
    db.create_all()


@manager.command
def dropdb():
    """Drops the db tables."""
    db.drop_all()


@manager.option('-u', '--username', dest='username', required=True)
@manager.option('-p', '--password', dest='password', required=True)
@manager.option('-e', '--email', dest='email', required=True)
def adduser(username=None, password=None, email=None):
    user = User(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('user was created')


if __name__ == '__main__':
    manager.run()