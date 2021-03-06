from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
from werkzeug.exceptions import HTTPException


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    from model import db
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()
application = app  # for AWS EB
cors = CORS(app, resources={r"*": {"origins": "*"}})
cache = Cache(app)

import route.nucleotide

@app.errorhandler(Exception)
def server_error(e):
    if isinstance(e, HTTPException):
        return e
    return jsonify(error=repr(e)), 500

@app.after_request
def add_header(response):
    response.cache_control.max_age = app.config['RESPONSE_CACHE_CONTROL_MAX_AGE']
    response.cache_control.public = app.config['RESPONSE_CACHE_CONTROL_PUBLIC']
    return response
