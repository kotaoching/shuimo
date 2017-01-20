# -*- coding: utf-8 -*-

from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from shuimo.models import User

RESERVED_WORDS = [
    'root', 'admin', 'bot', 'robot', 'master', 'webmaster',
    'account', 'people', 'user', 'users', 'project', 'projects',
    'search', 'action', 'favorite', 'like', 'love', 'none',
    'team', 'teams', 'group', 'groups', 'organization',
    'organizations', 'package', 'packages', 'org', 'com', 'net',
    'help', 'doc', 'docs', 'document', 'documentation', 'blog',
    'bbs', 'forum', 'forums', 'static', 'assets', 'repository',

    'public', 'private',
    'mac', 'windows', 'ios', 'lab',
]


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=20),
        Regexp(r'^[a-z0-9A-Z]+$')
    ])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])

    def validate_username(self, field):
        data = field.data.lower()
        if data in RESERVED_WORDS:
            raise ValueError('This name is a reserved name.')
        if data in current_app.config.get('RESERVED_WORDS', []):
            raise ValueError('This name is a reserved name.')
        if User.query.filter_by(username=data).count():
            raise ValueError('This name has been registered.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).count():
            raise ValueError('This email has been registered.')

    def save(self, role=None):
        user = User(**self.data)
        if role:
            user.role = 0
        user.save()
        return user


class SigninForm(FlaskForm):
    account = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_password(self, field):
        account = self.account.data
        if '@' in account:
            user = User.query.filter_by(email=account).first()
        else:
            user = User.query.filter_by(username=account).first()

        if not user:
            raise ValueError('Wrong account or password')
        if user.check_password(field.data):
            self.user = user
            return user
        raise ValueError('Wrong account or password')