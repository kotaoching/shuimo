# -*- coding: utf-8 -*-

from flask import jsonify
from shuimo.controllers.base import RegisterUnifiedRoute
from shuimo.models import User

admin = RegisterUnifiedRoute('users')


@admin.route('')
def users():
    users = User.query.all()

    data = []
    for item in users:
        user = item.to_dict()
        data.append(user)

    return jsonify(data=data)