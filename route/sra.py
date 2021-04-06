from flask import jsonify, request, Response
from flask import current_app as app
from query import get_analysis_index


@app.route('/index/run=<run_id>')
def get_index_run_route(run_id):
    return jsonify(get_analysis_index(run_id))
