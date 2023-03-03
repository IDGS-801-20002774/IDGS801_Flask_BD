import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True

    # Es la cadena de conexión que se ocupará:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False