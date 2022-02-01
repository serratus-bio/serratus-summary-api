from flask import jsonify, request, Response
from flask import current_app as app
from query import get_palmprint

@app.route('/palmprint/run=<run_id>')
def get_palmprint_run_route(run_id):
    return jsonify(get_palmprint(run_id))
