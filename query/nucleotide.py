from flask_sqlalchemy_caching import FromCache
from model.nucleotide import nsra, nfamily, nsequence
from . import apply_filters
from application import cache


# sra

def get_sra_properties(sra):
    query = nsra.query.filter(nsra.sra_id == sra)
    return query.one()

def get_sra_families(sra):
    query = nfamily.query.filter(nfamily.sra_id == sra)
    return query.all()

def get_sra_sequences(sra):
    query = nsequence.query.filter(nsequence.sra_id == sra)
    return query.all()

# matches

tableMap = {
    'family': nfamily,
    'genbank': nsequence
}

def get_matches(**url_params):
    if 'family' in url_params:
        key = 'family'
    elif 'genbank' in url_params:
        key = 'genbank'

    value = url_params.pop(key)
    table = tableMap[key]
    filter_col = getattr(table, table.filter_col_name)

    query = (table.query
        .filter(filter_col == value)
        .with_entities(table.sra_id)
        .options(FromCache(cache)))
    query = apply_filters(query, table, **url_params)
    sra_ids = (row[0] for row in query.all())
    return sra_ids

def get_matches_paginated(page=1, perPage=20, **url_params):
    page = int(page)
    perPage = int(perPage)
    if 'family' in url_params:
        key = 'family'
    elif 'genbank' in url_params:
        key = 'genbank'

    value = url_params.pop(key)
    table = tableMap[key]
    filter_col = getattr(table, table.filter_col_name)

    query = (table.query
        .filter(filter_col == value)
        .order_by(table.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, table, **url_params)
    return query.paginate(page, perPage)
