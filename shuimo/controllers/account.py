# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import session
from flask import redirect, render_template, url_for
from ..models import db, User
from ..forms import RegisterForm, LoginForm

bp = Blueprint('account', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data,
                    form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('account/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        session['user_id'] = form.user.id
        return redirect('/')
    return render_template('account/login.html', form=form)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))