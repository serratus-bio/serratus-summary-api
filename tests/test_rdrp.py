import application
from model.tables.rdrp import rsra, rphylum, rfamily, rdrp
from query import rdrp_query


def test_run_summary():
    result = rdrp_query.get_summary('ERR2756788')
    assert type(result['properties']) == rsra
    assert len(result['phylums']) == 6
    assert len(result['families']) == 65
    assert len(result['sequences']) == 123


def test_download_phylum():
    contents = rdrp_query.get_matches_file(phylum='Pisuviricota', scoreMin=100)
    with open('tests/files/SerratusMatches-rdrp-phylum-Pisuviricota.csv') as f:
        assert contents == f.read()


def test_download_sequence():
    pass


def test_paginate_phylum():
    pagination = rdrp_query.get_matches_paginated(phylum='Pisuviricota', scoreMin=100)
    assert len(pagination.items) == 20
    assert pagination.items[0] == rphylum(run_id='SRR9320190', phylum_name='Pisuviricota', coverage_bins='UWAOOAAAAOOAAOAAOAAOMOAAm', score=100, percent_identity=61, depth=2064.0, n_reads=23389, aligned_length=44)
    assert pagination.total == 65352


def test_paginate_family():
    pagination = rdrp_query.get_matches_paginated(family='Coronaviridae', scoreMin=100)
    assert len(pagination.items) == 20
    assert pagination.items[0] == rfamily(run_id='DRR220589', phylum_name='Pisuviricota', family_name='Coronaviridae', family_group='Coronaviridae-1', coverage_bins='aaawaawawaawawaaawwuawwwa', score=100, percent_identity=97, depth=37.1, n_reads=405, aligned_length=46)
    assert pagination.total == 5310


def test_paginate_sequence():
    pagination = rdrp_query.get_matches_paginated(sequence='NC_001653', scoreMax=50)
    assert len(pagination.items) == 20
    assert pagination.items[0] == rdrp(run_id='SRR1595854', phylum_name='Deltavirus', family_name='Deltavirus', family_group='Deltavirus-1', virus_name='hdv1', sequence_accession='NC_001653', coverage_bins='_momauuu_woou_________ao_', score=49, percent_identity=81, depth=27.4, n_reads=447, aligned_length=31)
    assert pagination.total == 166


def test_counts():
    counts = rdrp_query.get_counts(family='Coronaviridae')
    assert len(counts) == 1387
    print(counts[10])
    assert counts[10] == {'score': 1, 'percent_identity': 77, 'count': 10}

    counts = rdrp_query.get_counts(sequence='NC_001653')
    assert len(counts) == 135
    assert counts[10] == {'score': 1, 'percent_identity': 89, 'count': 1}


def test_list():
    values_list = rdrp_query.get_list('family')
    assert len(values_list) == 2513

    values_list = rdrp_query.get_list('sequence')
    assert len(values_list) == 14669
