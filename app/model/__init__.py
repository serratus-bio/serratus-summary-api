from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy_caching import CachingQuery


db = SQLAlchemy(query_class=CachingQuery)
