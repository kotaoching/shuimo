# -*- coding: utf-8 -*-

from flask import jsonify
from shuimo.controllers.base import RegisterUnifiedRoute

api = RegisterUnifiedRoute('painting')


@api.route('')
def paintings():
    return 'resources'


@api.route('/<tid>')
def view_painting(tid):
    paintings = {'1': 'web', '2': 'ios', '3': 'mac'}

    if tid in paintings:
        return jsonify({tid: paintings[tid]})
    else:
        return tid


@api.route('/subject/<tid>')
def view_subject(tid):
    paintings = {'1': 'web', '2': 'ios', '3': 'mac'}

    if tid in paintings:
        return jsonify({tid: paintings[tid]})
    else:
        return tid