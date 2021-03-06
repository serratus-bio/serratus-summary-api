import os
import tempfile
import pytest

import application
from model.nucleotide import nsra, nfamily, nsequence
from query.nucleotide import (
    get_run_properties,
    get_run_families,
    get_run_sequences,
    get_matches_file,
    get_matches_paginated,
    get_counts,
)
from route.nucleotide import get_run_route, run_cache


def test_run_summary():
    result = get_run_properties('ERR2756788')
    assert result == nsra(sra_id='ERR2756788', read_length=150, genome='cov3ma', version='200818', date='200817-21:05')

    result = get_run_families('ERR2756788')
    assert len(result) == 12
    assert result[0] == nfamily(sra_id='ERR2756788', family_name='AMR', coverage_bins='mooaoooUmmmmmooooaaoawwwm', score=100, percent_identity=97, depth=214.8, n_reads=1382, n_global_reads=301, length=1000)

    result = get_run_sequences('ERR2756788')
    assert len(result) == 349
    assert result[0] == nsequence(sra_id='ERR2756788', family_name='Coronaviridae', genbank_id='HQ728485.1', coverage_bins=':a..__uu__a_________o____', score=28, percent_identity=85, depth=0.7, n_reads=119, n_global_reads=98, length=13015, genbank_name='Miniopterus bat coronavirus/Kenya/KY33/2006 polyprotein (ORF1ab) gene, partial cds; and spike protein (S), ORF3 protein (ORF3), envelope protein (E), membrane protein (M), nucleocapsid protein (N), and hypothetical protein ORFx (ORFx) genes, complete cds')


def test_run_cache():
    orig = get_run_route('ERR2756788')
    cache = run_cache.get('ERR2756788')
    assert orig.data == cache.data


def test_download_family():
    contents = get_matches_file(family='Coronaviridae', scoreMin=100)
    with open('tests/SerratusMatches-family.csv') as f:
        assert contents == f.read()


def test_download_genbank():
    contents = get_matches_file(genbank='EU769558.1', scoreMax=50)
    with open('tests/SerratusMatches-genbank.csv') as f:
        assert contents == f.read()


def test_paginate_family():
    pagination = get_matches_paginated(family='Coronaviridae', scoreMin=100)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nfamily(sra_id='SRR9966511', family_name='Coronaviridae', coverage_bins='mUmmUmmmUmUmmUmmUUmmUmUmm', score=100, percent_identity=99, depth=14.9, n_reads=2923, n_global_reads=401, length=30000)
    assert pagination.total == 2839

    pagination = get_matches_paginated(family='Coronaviridae', scoreMin=100, perPage=3)
    assert len(pagination.items) == 3


def test_paginate_genbank():
    pagination = get_matches_paginated(genbank='EU769558.1', scoreMax=50)
    assert len(pagination.items) == 20
    assert pagination.items[0] == nsequence(sra_id='ERR2756788', family_name='Coronaviridae', genbank_id='EU769558.1', coverage_bins='aUAUmmm__________________', score=45, percent_identity=85, depth=9.6, n_reads=1694, n_global_reads=399, length=14335, genbank_name='Bat coronavirus Trinidad/1CO7BA/2007 nonstructural protein 1b` gene, partial cds')
    assert pagination.total == 365

    pagination = get_matches_paginated(genbank='EU769558.1', scoreMax=50, perPage=3)
    assert len(pagination.items) == 3


def test_counts():
    counts = get_counts(family='Coronaviridae')
    assert len(counts) == 1320
    assert counts[10] == {'score': 1, 'percent_identity': 97, 'count': 43356}

    counts = get_counts(genbank='EU769558.1')
    assert len(counts) == 43
    print(counts[10])
    assert counts[10] == {'score': 1, 'percent_identity': 100, 'count': 201}
