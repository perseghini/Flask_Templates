import os

DEBUG = True
SECRET_KEY = 'Use a better secret key than this!'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                      'flask_templates.db')