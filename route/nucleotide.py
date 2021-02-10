from flask import jsonify, request
from flask import current_app as app
from query.nucleotide import (
    get_sra_properties,
    get_sra_families,
    get_sra_sequences,
    get_family_pagination,
    get_genbank_pagination
)
from werkzeug.contrib.cache import SimpleCache
from config import CACHE_DEFAULT_TIMEOUT


sra_cache = SimpleCache()

@app.route('/nucleotide/sra=<sra>')
def get_sra(sra):
    return get_sra_cache(sra)


@app.route('/nucleotide/family=<family>')
def get_family(family):
    pagination = get_family_pagination(family, **request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)


@app.route('/nucleotide/genbank=<genbank>')
def get_genbank(genbank):
    pagination = get_genbank_pagination(genbank, **request.args)
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
