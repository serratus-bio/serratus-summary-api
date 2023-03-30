from flask import jsonify, request, Response
from flask import current_app as app
from query import get_analysis_index
from application import cache


@app.route('/index/run=<run_id>')
@cache.cached(query_string=True)
def get_index_run_route(run_id):
    return jsonify(get_analysis_index(run_id))
