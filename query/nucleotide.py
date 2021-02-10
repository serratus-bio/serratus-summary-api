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

# family

def get_family_pagination(family, page=1, perPage=20, **kwargs):
    page = int(page)
    perPage = int(perPage)
    query = (nfamily.query
        .filter(nfamily.family_name == family)
        .order_by(nfamily.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, nfamily, **kwargs)
    return query.paginate(page, perPage)

# genbank

def get_genbank_pagination(genbank, page=1, perPage=20, **kwargs):
    page = int(page)
    perPage = int(perPage)
    query = (nsequence.query
        .filter(nsequence.genbank_id == genbank)
        .order_by(nsequence.score.desc())
        .options(FromCache(cache)))
    query = apply_filters(query, nsequence, **kwargs)
    return query.paginate(page, perPage)
