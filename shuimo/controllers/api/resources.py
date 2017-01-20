# -*- coding: utf-8 -*-

from flask import jsonify
from shuimo.controllers.base import RegisterUnifiedRoute

api = RegisterUnifiedRoute('resources')


@api.route('')
def topics():
    return 'resources'


@api.route('/<tid>')
def view_topic(tid):
    topics = {'1': 'web', '2': 'ios', '3': 'mac'}

    if tid in topics:
        return jsonify({tid: topics[tid]})
    else:
        return tid