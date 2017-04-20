# config.py

import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True
APP_DEBUG = True
CSRF_ENABLED = True
WTF_CSRF_ENABLED = True

# Enables automatic commits to database changes at the end of each request
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

try:
    from local_settings import *
except ImportError:
    pass
