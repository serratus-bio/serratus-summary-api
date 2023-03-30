from flask import jsonify, request, Response
from flask import current_app as app
from query import get_palmprint
from application import cache


@app.route('/palmprint/run=<run_id>')
@cache.cached(query_string=True)
def get_palmprint_run_route(run_id):
    return jsonify(get_palmprint(run_id))
