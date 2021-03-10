from flask import jsonify, request
from flask import current_app as app
from query.nucleotide import (
    get_counts,
)

@app.route('/counts/nucleotide')
def get_counts_route():
    counts = get_counts(**request.args)
    return jsonify(counts)
