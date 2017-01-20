# -*- coding: utf-8 -*-

from functools import wraps
from flask import g, request, session
from flask import redirect, url_for
from shuimo.models import User


def get_current_user():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if not user:
            return None
        return user
    return None


def signin_user(user, permanent=False):
    if not user:
        return None
    session['user_id'] = user.id
    if permanent:
        session.permanent = True
    return user


def signout_user():
    if 'user_id' not in session:
        return
    session.pop('user_id')


def require_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('signin', next=request.url))
        return f(*args, **kwargs)
    return wrapper