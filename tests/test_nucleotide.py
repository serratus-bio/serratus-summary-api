from . import get_response_data, get_response_json

def test_run_summary():
    first_page = get_response_json("/matches/nucleotide/run/paged?run=ERR2756788&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['coverage_bins', str],
        ['depth', float],
        ['family_id', str],
        ['family_name', str],
        ['length', int],
        ['n_global_reads', int],
        ['n_reads', int],
        ['percent_identity', int],
        ['run_id', str],
        ['score', int]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/nucleotide/run/paged?run=ERR2756788&page=2&perPage=5")
    assert len(second_page['result']) == 5
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

# def test_matches_download_family():
#     contents = get_response_data("/matches/nucleotide/download?family=Coronaviridae&scoreMin=100")
#     with open('tests/files/SerratusMatches-nucleotide-family-Coronaviridae.csv') as f:
#         assert contents == f.read()

# def test_matches_download_sequence():
#     contents = get_response_data("/matches/nucleotide/download?sequence=EU769558.1&scoreMax=50")
#     with open('tests/files/SerratusMatches-nucleotide-sequence-EU769558.1.csv') as f:
#         assert contents == f.read()

def test_matches_family():
    result = get_response_json("/matches/nucleotide?family=Coronaviridae&scoreMin=100&columns=run_id")
    assert 'run_id' in result[0]
    assert isinstance('run_id', str)

def test_paginate_family():
    first_page = get_response_json("/matches/nucleotide/paged?family=Coronaviridae&scoreMin=100&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['coverage_bins', str],
        ['depth', float],
        ['family_id', str],
        ['family_name', str],
        ['length', int],
        ['n_global_reads', int],
        ['n_reads', int],
        ['percent_identity', int],
        ['run_id', str],
        ['score', int]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/nucleotide/paged?family=Coronaviridae&scoreMin=100&page=2&perPage=5")
    assert len(second_page['result']) == 5

    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

def test_paginate_sequence():
    first_page = get_response_json("/matches/nucleotide/paged?sequence=EU769558.1&scoreMax=50&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['coverage_bins', str],
        ['depth', float],
        ['family_id', str],
        ['family_name', str],
        ['length', int],
        ['n_global_reads', int],
        ['n_reads', int],
        ['percent_identity', int],
        ['run_id', str],
        ['score', int],
        ['sequence_accession', str],
        ['virus_name', str]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/nucleotide/paged?sequence=EU769558.1&scoreMax=50&page=2&perPage=5")
    assert len(second_page['result']) == 5

    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

def test_counts():
    result = get_response_json("/counts/nucleotide?family=Coronaviridae")

    for [key, type] in [
        ['count', int],
        ['percent_identity', int],
        ['score', int]
    ]:
      assert key in result['result'][0]
      assert isinstance(result['result'][0][key], type)

# def test_list():
#     values_list = get_response_json("/list/nucleotide/family")
#     assert len(values_list) == 46

#     values_list = get_response_json("/list/nucleotide/sequence")
#     assert len(values_list) == 13187
