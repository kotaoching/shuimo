# -*- coding: utf-8 -*-

from functools import wraps
from flask import g, request, session
from flask import redirect, url_for
from ..models import User


def get_current_user():
    if 'id' in session and 'token' in session:
        user = User.query.get(session['id'])
        if not user:
            return None
        if user.token != session['token']:
            return None
        return user
    return None


def signin_user(user, permanent=False):
    if not user:
        return None
    session['id'] = user.id
    session['token'] = user.token
    if permanent:
        session.permanent = True
    return user


def signout_user():
    if 'id' not in session:
        return
    session.pop('id')
    session.pop('token')


def require_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('signin', next=request.url))
        return f(*args, **kwargs)
    return wrapper