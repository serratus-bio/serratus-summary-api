from . import get_response_data, get_response_json


def test_run_summary():
    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&perPage=10")
    assert len(pagination['result']) == 10

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&scoreMin=20")
    assert pagination['total'] == 5

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&family=Coronaviridae-1")
    assert pagination['total'] == 13

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&family=Coronaviridae-1&scoreMin=20")
    assert pagination['total'] == 2


def test_download_phylum():
    contents = get_response_data("/matches/rdrp?phylum=Pisuviricota&scoreMin=100")
    with open('tests/files/SerratusMatches-rdrp-phylum-Pisuviricota.csv') as f:
        assert contents == f.read()


def test_download_sequence():
    pass


def test_paginate_phylum():
    pagination = get_response_json("/matches/rdrp/paged?phylum=Pisuviricota&scoreMin=100")
    assert len(pagination['result']) == 20
    assert pagination['result'][0] == {'run_id': 'SRR9320190', 'phylum_name': 'Pisuviricota', 'coverage_bins': 'UWAOOAAAAOOAAOAAOAAOMOAAm', 'score': 100, 'percent_identity': 61, 'depth': 2064.0, 'n_reads': 23389, 'aligned_length': 44}
    assert pagination['total'] == 65352


def test_paginate_family():
    pagination = get_response_json("/matches/rdrp/paged?family=Coronaviridae&scoreMin=100")
    assert len(pagination['result']) == 20
    assert pagination['result'][0] == {'run_id': 'DRR220589', 'phylum_name': 'Pisuviricota', 'family_name': 'Coronaviridae', 'family_group': 'Coronaviridae-1', 'family_id': 'Coronaviridae-1', 'coverage_bins': 'aaawaawawaawawaaawwuawwwa', 'score': 100, 'percent_identity': 97, 'depth': 37.1, 'n_reads': 405, 'aligned_length': 46}
    assert pagination['total'] == 5310


def test_paginate_sequence():
    data = get_response_json("/matches/rdrp/paged?sequence=NC_001653&scoreMax=50")
    assert len(data['result']) == 20
    assert data['result'][0] == {'run_id': 'SRR1595854', 'phylum_name': 'Deltavirus', 'family_name': 'Deltavirus', 'family_group': 'Deltavirus-1', 'family_id': 'Deltavirus-1', 'virus_name': 'hdv1', 'sequence_accession': 'NC_001653', 'coverage_bins': '_momauuu_woou_________ao_', 'score': 49, 'percent_identity': 81, 'depth': 27.4, 'n_reads': 447, 'aligned_length': 31}
    assert data['total'] == 166


def test_counts():
    counts = get_response_json("/counts/rdrp?family=Coronaviridae")
    assert len(counts) == 1387
    assert counts[10] == {'score': 1, 'percent_identity': 77, 'count': 10}

    counts = get_response_json("/counts/rdrp?sequence=NC_001653")
    assert len(counts) == 135
    assert counts[10] == {'score': 1, 'percent_identity': 89, 'count': 1}


def test_list():
    values_list = get_response_json("/list/rdrp/family")
    assert len(values_list) == 2513

    values_list = get_response_json("/list/rdrp/sequence")
    assert len(values_list) == 14669
