import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'cmaaaaaan'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# 
# OAUTH_CREDENTIALS = [
#     {
#         'facebook': {
#             'id': '470154729788964',
#             'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
#         },
#         'twitter': {
#             'id': '3RzWQclolxWZIMq5LJqzRZPTl',
#             'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
#         }
#     }
# ]
