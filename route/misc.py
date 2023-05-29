from flask import jsonify, request
from flask import current_app as app
from application import cache

@app.route('/favicon.ico')
@cache.cached(query_string=True)
def get_favicon_ico():
    return jsonify(True)
