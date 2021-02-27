from flask import jsonify, request, Response
from flask import current_app as app
from query.nucleotide import (
    get_sra_properties,
    get_sra_families,
    get_sra_sequences,
    get_matches,
    get_matches_paginated,
)
from cachelib.simple import SimpleCache
from config import CACHE_DEFAULT_TIMEOUT


sra_cache = SimpleCache()

@app.route('/summary/nucleotide/sra=<sra>')
def get_sra_route(sra):
    return get_sra_cache(sra)

@app.route('/matches/nucleotide')
def get_matches_route():
    sra_ids = get_matches(**request.args)
    return Response('\n'.join(sra_ids), mimetype='text/plain')

@app.route('/matches/nucleotide/paged')
def get_matches_paginated_route():
    pagination = get_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)

def get_sra_cache(sra):
    response = sra_cache.get(sra)
    if response:
        return response
    properties = get_sra_properties(sra)
    families = get_sra_families(sra)
    sequences = get_sra_sequences(sra)
    response = jsonify(properties=properties, families=families, sequences=sequences)
    sra_cache.set(sra, response, timeout=CACHE_DEFAULT_TIMEOUT)
    return response
