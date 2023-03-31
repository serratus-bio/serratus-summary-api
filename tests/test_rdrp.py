import pytest
from . import get_response_data, get_response_json


def test_run_summary():
    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&perPage=10")
    assert len(pagination['result']) == 10

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&scoreMin=20")
    assert pagination['total'] == 5

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&familyId=Tombusviridae-14")
    assert pagination['total'] == 20

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&familyName=Tombusviridae")
    assert pagination['total'] == 36

    pagination = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&familyId=Tombusviridae-14&scoreMin=20")
    assert pagination['total'] == 1

    with pytest.raises(Exception):
        get_response_json("/matches/rdrp/run/paged?run=ERR2756788&familyName=Tombusviridae&familyId=Tombusviridae-14&scoreMin=20")


def test_download_phylum():
    contents = get_response_data("/matches/rdrp/download?phylum=Pisuviricota&scoreMin=100")
    with open('tests/files/SerratusMatches-rdrp-phylum-Pisuviricota.csv') as f:
        assert contents == f.read()


def test_download_sequence():
    pass


def test_paginate_phylum():
    pagination = get_response_json("/matches/rdrp/paged?phylum=Pisuviricota&scoreMin=100")
    assert len(pagination['result']) == 20
    assert pagination['result'][0] == {'run_id': 'SRR5633706', 'phylum_name': 'Pisuviricota', 'coverage_bins': '^^^^^^^^^^^^^^^^^^^^^^^^^', 'score': 100, 'percent_identity': 98, 'depth': 64096.8, 'n_reads': 998569, 'aligned_length': 32}
    assert pagination['total'] == 65352


def test_paginate_family():
    pagination = get_response_json("/matches/rdrp/paged?family=Coronaviridae&scoreMin=100")
    assert len(pagination['result']) == 20
    assert pagination['result'][0] == {'run_id': 'SRR12348234', 'phylum_name': 'Pisuviricota', 'family_name': 'Coronaviridae', 'family_group': 'Coronaviridae-1', 'family_id': 'Coronaviridae-1', 'coverage_bins': 'MMOAM^AOM^^^^^^^^^^^^^^mw', 'score': 100, 'percent_identity': 99, 'depth': 94113.8, 'n_reads': 996256, 'aligned_length': 47}
    assert pagination['total'] == 5310


def test_paginate_family_unique():
    pagination1 = get_response_json("/matches/rdrp/paged?page=1&perPage=10&scoreMin=72&scoreMax=100&identityMin=50&identityMax=87&family=Bornaviridae")
    matches1 =set(match['run_id'] for match in pagination1['result'])
    pagination2 = get_response_json("/matches/rdrp/paged?page=2&perPage=10&scoreMin=72&scoreMax=100&identityMin=50&identityMax=87&family=Bornaviridae")
    matches2 =set(match['run_id'] for match in pagination2['result'])
    assert len(matches1 & matches2) == 0


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
