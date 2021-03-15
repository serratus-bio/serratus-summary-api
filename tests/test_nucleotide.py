import application
from model.tables.nucleotide import nsra, nfamily, nsequence
from query import nucleotide_query


def test_run_summary():
    result = nucleotide_query.get_summary('ERR2756788')
    assert type(result['properties']) == nsra
    assert len(result['families']) == 12
    assert len(result['sequences']) == 349


def test_download_family():
    contents = nucleotide_query.get_matches_file(family='Coronaviridae', scoreMin=100)
    with open('tests/files/SerratusMatches-nucleotide-family-Coronaviridae.csv') as f:
        assert contents == f.read()


def test_download_genbank():
    contents = nucleotide_query.get_matches_file(genbank='EU769558.1', scoreMax=50)
    with open('tests/files/SerratusMatches-nucleotide-genbank-EU769558.1.csv') as f:
        assert contents == f.read()


def test_paginate_family():
    pagination = nucleotide_query.get_matches_paginated(family='Coronaviridae', scoreMin=100)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nfamily(run_id='SRR9966511', family_name='Coronaviridae', coverage_bins='mUmmUmmmUmUmmUmmUUmmUmUmm', score=100, percent_identity=99, depth=14.9, n_reads=2923, n_global_reads=401, length=30000)
    assert pagination.total == 2839

    pagination = nucleotide_query.get_matches_paginated(family='Coronaviridae', scoreMin=100, perPage=3)
    assert len(pagination.items) == 3


def test_paginate_genbank():
    pagination = nucleotide_query.get_matches_paginated(genbank='EU769558.1', scoreMax=50)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nsequence(run_id='ERR2756788', family_name='Coronaviridae', genbank_id='EU769558.1', coverage_bins='aUAUmmm__________________', score=45, percent_identity=85, depth=9.6, n_reads=1694, n_global_reads=399, length=14335, genbank_name='Bat coronavirus Trinidad/1CO7BA/2007 nonstructural protein 1b` gene, partial cds')
    assert pagination.total == 365

    pagination = nucleotide_query.get_matches_paginated(genbank='EU769558.1', scoreMax=50, perPage=3)
    assert len(pagination.items) == 3


def test_counts():
    counts = nucleotide_query.get_counts(family='Coronaviridae')
    assert len(counts) == 1320
    assert counts[10] == {'score': 1, 'percent_identity': 97, 'count': 43356}

    counts = nucleotide_query.get_counts(genbank='EU769558.1')
    assert len(counts) == 43
    assert counts[10] == {'score': 1, 'percent_identity': 100, 'count': 201}


def test_list():
    values_list = nucleotide_query.get_list('family')
    assert len(values_list) == 46

    values_list = nucleotide_query.get_list('genbank')
    assert len(values_list) == 13187
