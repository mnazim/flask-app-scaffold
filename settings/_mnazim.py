from .base import *


DEBUG = True
SECRET_KEY = 'my-super-secret-key'
SQLALCHEMY_DATABASE_URI = 'postgres://pguser:password@localhost/nlib'
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'my-super-secret-password-salt'
SECURITY_REGISTERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_SEND_REGISTER_EMAIL = False