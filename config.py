import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'cmaaaaaan'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '470154729788964',
        'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
    },
    'twitter': {
        'id': 'hQnYgKRy6vQ5grvus1QTRvKfs',
        'secret': 'FqVvQOT9dIckaZVz1lDZWwQmWhwRENCKgly5f2o3hSlHdglJga'
    }
}
