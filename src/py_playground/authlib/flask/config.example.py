import os

SECRET_KEY = os.urandom(32)

GOOGLE_CLIENT_KEY = ''
GOOGLE_CLIENT_SECRET = ''

SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
SQLALCHEMY_TRACK_MODIFICATIONS = False
