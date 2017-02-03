import os

# grab folder where script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
# WTF_ is a security measure supported by Flask; we should always try to use it
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

# define full path for DB, this is SUPER IMPORTANT because it is the \
# trail of breadcrums the app will follow to find the databse path in this file
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
