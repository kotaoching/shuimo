# -*- coding: utf-8 -*-

DEBUG = False
TESTING = False

#: session
SESSION_COOKIE_NAME = '_m_session'
# SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

#: account
SECRET_KEY = 'secret key'
PASSWORD_SECRET = 'password secrte'

#: sqlalchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/shuimo'

#: email settings
# MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 25
# MAIL_USE_SSL = True
# MAIL_USERNAME = ''
# MAIL_PASSWORD = ''
# MAIL_DEFAULT_SENDER = ('name', 'noreply@email.com')