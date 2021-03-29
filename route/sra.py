from flask import jsonify, request, Response
from flask import current_app as app
from query import sra_query


@app.route('/index/run=<run_id>')
def get_index_run_route(run_id):
    return jsonify(**sra_query.get_index(run_id))
