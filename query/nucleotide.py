from flask_sqlalchemy_caching import FromCache
from model.nucleotide import nsra, nfamily, nsequence
from . import apply_filters
from application import cache


# SRA run summary

def get_run_properties(run_id):
    query = nsra.query.filter(nsra.sra_id == run_id)
    return query.one()

def get_run_families(run_id):
    query = nfamily.query.filter(nfamily.sra_id == run_id)
    return query.all()

def get_run_sequences(run_id):
    query = nsequence.query.filter(nsequence.sra_id == run_id)
    return query.all()

# matches

# url param key : table model
tableMap = {
    'family': nfamily,
    'genbank': nsequence
}

def get_table_key(**url_params):
    for key in tableMap:
        if key in url_params:
            return key

def get_matches(**url_params):
    key = get_table_key(**url_params)
    value = url_params.pop(key)
    table = tableMap[key]
    filter_col = getattr(table, table.filter_col_name)
    query = (table.query
        .filter(filter_col == value)
        .with_entities(table.sra_id)
        .options(FromCache(cache)))
    query = apply_filters(query, table, **url_params)
    run_ids = (row[0] for row in query.all())
    return run_ids

def get_matches_paginated(page=1, perPage=20, **url_params):
    key = get_table_key(**url_params)
    value = url_params.pop(key)
    table = tableMap[key]
    filter_col = getattr(table, table.filter_col_name)
    query = (table.query
        .filter(filter_col == value)
        .order_by(table.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, table, **url_params)
    return query.paginate(int(page), int(perPage))
