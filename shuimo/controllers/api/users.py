# -*- coding: utf-8 -*-

from flask import jsonify
from .._base import RegisterRoute

api = RegisterRoute('users')


@api.route('/<userid>')
def users(userid):
    users = {'1': 'john', '2': 'steve', '3': 'bill'}

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return userid
