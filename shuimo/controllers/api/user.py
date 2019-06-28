# -*- coding: utf-8 -*-

from flask import jsonify
from sqlalchemy import func
from shuimo.controllers.base import RegisterUnifiedRoute
from shuimo.models import User
from shuimo.utils.account import get_current_user

api = RegisterUnifiedRoute('user')


@api.route('/<username>')
def users(username):
    user = User.query.filter(func.lower(User.username) == username.lower()).first()

    if user:
        return jsonify(data=user.to_dict())
    else:
        return jsonify(data=[])


@api.route('/me')
def me():
    user = get_current_user()

    return jsonify(data=user.to_dict())