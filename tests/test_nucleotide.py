from . import get_response_data, get_response_json

def test_run_summary():
    first_page = get_response_json("/matches/nucleotide/run/paged?run=ERR2756788&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['coverage_bins', str],
        ['depth', float],
        ['family_id', str],
        ['family_name', str],
        ['length', float],
        ['n_global_reads', float],
        ['n_reads', float],
        ['percent_identity', float],
        ['run_id', str],
        ['score', float]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)
    
    second_page = get_response_json("/matches/nucleotide/run/paged?run=ERR2756788&page=2perPage=5")
    
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


# def test_matches_family():
#     result = get_response_json("/matches/nucleotide?family=Coronaviridae&scoreMin=100&columns=run_id")
#     assert result[0] == {
#         'run_id': 'SRR1192321',
#     }


# def test_paginate_family():
#     pagination = get_response_json("/matches/nucleotide/paged?family=Coronaviridae&scoreMin=100")
#     assert len(pagination['result']) == 20
#     assert pagination['result'][0] == {'run_id': 'SRR1192321', 'family_name': 'Coronaviridae', 'family_id': 'Coronaviridae', 'coverage_bins': '^^^^^^^^^^^^^^^^^^^^^^^^^', 'score': 100, 'percent_identity': 100, 'depth': 177221.0, 'n_reads': 133710950, 'n_global_reads': 2790072, 'length': 30000}
#     assert pagination['total'] == 2839

#     pagination = get_response_json("/matches/nucleotide/paged?family=Coronaviridae&scoreMin=100&perPage=3")
#     assert len(pagination['result']) == 3


# def test_paginate_sequence():
#     pagination = get_response_json("/matches/nucleotide/paged?sequence=EU769558.1&scoreMax=50")
#     assert len(pagination['result']) == 20
#     assert pagination['result'][0] == {'run_id': 'ERR2756788', 'family_name': 'Coronaviridae', 'family_id': 'Coronaviridae', 'sequence_accession': 'EU769558.1', 'coverage_bins': 'aUAUmmm__________________', 'score': 45, 'percent_identity': 85, 'depth': 9.6, 'n_reads': 1694, 'n_global_reads': 399, 'length': 14335, 'virus_name': 'Bat coronavirus Trinidad/1CO7BA/2007 nonstructural protein 1b` gene, partial cds'}
#     assert pagination['total'] == 365

#     pagination = get_response_json("/matches/nucleotide/paged?sequence=EU769558.1&scoreMax=50&perPage=3")
#     assert len(pagination['result']) == 3


# def test_counts():
#     counts = get_response_json("/counts/nucleotide?family=Coronaviridae")
#     assert len(counts) == 1320
#     assert counts[10] == {'score': 1, 'percent_identity': 97, 'count': 43356}

#     counts = get_response_json("/counts/nucleotide?sequence=EU769558.1")
#     assert len(counts) == 43
#     assert counts[10] == {'score': 1, 'percent_identity': 100, 'count': 201}


# def test_list():
#     values_list = get_response_json("/list/nucleotide/family")
#     assert len(values_list) == 46

#     values_list = get_response_json("/list/nucleotide/sequence")
#     assert len(values_list) == 13187
