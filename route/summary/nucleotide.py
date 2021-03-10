from flask import jsonify
from flask import current_app as app
from query.nucleotide import (
    get_run_properties,
    get_run_families,
    get_run_sequences,
)
from cachelib.simple import SimpleCache
from config import CACHE_DEFAULT_TIMEOUT


run_cache = SimpleCache()


def get_run_cache(run_id):
    response = run_cache.get(run_id)
    if response:
        return response
    properties = get_run_properties(run_id)
    families = get_run_families(run_id)
    sequences = get_run_sequences(run_id)
    response = jsonify(properties=properties, families=families, sequences=sequences)
    run_cache.set(run_id, response, timeout=CACHE_DEFAULT_TIMEOUT)
    return response


@app.route('/summary/nucleotide/run=<run_id>')
def get_run_route(run_id):
    return get_run_cache(run_id)
