import pytest
from . import get_response_data, get_response_json

def test_run_summary():
    first_page = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['aligned_length', int],
        ['coverage_bins', str],
        ['depth', float],
        ['family_group', str],
        ['family_id', str],
        ['family_name', str],
        ['n_reads', int],
        ['percent_identity', int],
        ['phylum_name', str],
        ['run_id', str],
        ['score', int]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/rdrp/run/paged?run=ERR2756788&page=2&perPage=5")
    assert len(second_page['result']) == 5
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

# def test_matches_download_phylum():
#     contents = get_response_data("/matches/rdrp/download?phylum=Pisuviricota&scoreMin=100&columns=run_id")
#     with open('tests/files/SerratusMatches-rdrp-phylum-Pisuviricota.csv') as f:
#         assert contents == f.read()

def test_matches_phylum():
    result = get_response_json("/matches/rdrp?phylum=Pisuviricota&scoreMin=100&columns=run_id")
    assert 'run_id' in result[0]
    assert isinstance('run_id', str)

# def test_download_sequence():
#     pass # LOL

def test_paginate_phylum():
    first_page = get_response_json("/matches/rdrp/paged?phylum=Pisuviricota&scoreMin=100&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['aligned_length', int],
        ['coverage_bins', str],
        ['depth', float],
        ['n_reads', int],
        ['percent_identity', int],
        ['phylum_name', str],
        ['run_id', str],
        ['score', int]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/rdrp/paged?phylum=Pisuviricota&scoreMin=100&page=2&perPage=5")
    assert len(second_page['result']) == 5
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]


def test_paginate_family():
    first_page = get_response_json("/matches/rdrp/paged?family=Coronaviridae&scoreMin=100&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['aligned_length', int],
        ['coverage_bins', str],
        ['depth', float],
        ['family_group', str],
        ['family_id', str],
        ['family_name', str],
        ['n_reads', int],
        ['percent_identity', int],
        ['phylum_name', str],
        ['run_id', str],
        ['score', int]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/rdrp/paged?family=Coronaviridae&scoreMin=100&page=2&perPage=5")
    assert len(second_page['result']) == 5
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]


# def test_paginate_family_unique():
#     pagination1 = get_response_json("/matches/rdrp/paged?page=1&perPage=10&scoreMin=72&scoreMax=100&identityMin=50&identityMax=87&family=Bornaviridae")
#     matches1 =set(match['run_id'] for match in pagination1['result'])
#     pagination2 = get_response_json("/matches/rdrp/paged?page=2&perPage=10&scoreMin=72&scoreMax=100&identityMin=50&identityMax=87&family=Bornaviridae")
#     matches2 =set(match['run_id'] for match in pagination2['result'])
#     assert len(matches1 & matches2) == 0


# def test_paginate_sequence():
#     data = get_response_json("/matches/rdrp/paged?sequence=NC_001653&scoreMax=50")
#     assert len(data['result']) == 20
#     assert data['result'][0] == {
#         'run_id': 'ERR5869706',
#         'phylum_name': 'Deltavirus',
#         'family_name': 'Deltavirus',
#         'family_group': 'Deltavirus-1',
#         'family_id': 'Deltavirus-1',
#         'virus_name': 'hdv1',
#         'sequence_accession': 'NC_001653',
#         'coverage_bins': '_.:__.___u.:.:aoo:aomomo_',
#         'score': 49,
#         'percent_identity': 91,
#         'depth': 39.8,
#         'n_reads': 470,
#         'aligned_length': 42
#     }
#     assert data['total'] == 274


# def test_counts():
#     counts = get_response_json("/counts/rdrp?family=Coronaviridae")
#     assert len(counts) == 1387
#     assert counts[10] == {'score': 1, 'percent_identity': 77, 'count': 10}

#     counts = get_response_json("/counts/rdrp?sequence=NC_001653")
#     assert len(counts) == 135
#     assert counts[10] == {'score': 1, 'percent_identity': 89, 'count': 1}


# def test_list():
#     values_list = get_response_json("/list/rdrp/family")
#     assert len(values_list) == 2513

#     values_list = get_response_json("/list/rdrp/sequence")
#     assert len(values_list) == 14669
