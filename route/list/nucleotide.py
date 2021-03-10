from flask import jsonify, request
from flask import current_app as app
from query.nucleotide import (
    get_list,
)
from config import CACHE_DEFAULT_TIMEOUT


@app.route('/list/nucleotide/<query_type>')
def get_list_route(query_type):
    values_list = get_list(query_type, **request.args)
    return jsonify(values_list)
