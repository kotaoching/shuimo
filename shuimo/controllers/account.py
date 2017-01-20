# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import g, request, jsonify
from flask import redirect, render_template
from shuimo.models import db, User
from shuimo.forms import RegisterForm, SigninForm
from shuimo.utils.account import signin_user, signout_user

bp = Blueprint('account', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(form.username.data,
                    form.email.data,
                    form.password.data)
        user.save()
        signin_user(user)
        return jsonify({'username': user.username})
    return render_template('account/register.html', form=form)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    next_url = request.args.get('next', '/')
    if g.user:
        return redirect(next_url)
    form = SigninForm(csrf_enabled=False)
    if form.validate_on_submit():
        signin_user(form.user)
        return redirect(next_url)
    return render_template('account/signin.html', form=form)


@bp.route('/signout', methods=['GET', 'POST'])
def signout():
    next_url = request.args.get('next', '/')
    signout_user()
    return redirect(next_url)