import os


SQL_ENDPOINT = 'serratus-aurora-20210211-cluster.cluster-ro-ccz9y6yshbls.us-east-1.rds.amazonaws.com'
SQL_DATABASE = 'summary'
SQL_USERNAME = os.environ['SQL_USERNAME']
SQL_PASSWORD = os.environ['SQL_PASSWORD']
SQLALCHEMY_DATABASE_URI = f'postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_ENDPOINT}:5432/{SQL_DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False

CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 0
