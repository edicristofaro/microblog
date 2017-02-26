import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager(app)
lm.login_view = 'index'

from app import views, models

app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '470154729788964',
        'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
    },
    'twitter': {
        'id': 'hQnYgKRy6vQ5grvus1QTRvKfs',
        'secret': 'FqVvQOT9dIckaZVz1lDZWwQmWhwRENCKgly5f2o3hSlHdglJga'
    }
}
