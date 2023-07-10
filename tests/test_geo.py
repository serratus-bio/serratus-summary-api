from . import  get_response_json

def test_paginate_geo():
    first_page = get_response_json("/geo/rdrp/paged?page=1&perPage=10")
    assert len(first_page['result']) == 10

    for [key, type] in [
        ['biosample_id', str],
        ['coordinate_x', float],
        ['coordinate_y', float],
        ['from_text', str],
        ['release_date', str],
        ['run_id', str],
        ['scientific_name', str],
        ['tax_id', str]
    ]:
      assert key in first_page['result'][0]
      assert isinstance(first_page['result'][0][key], type)

    second_page = get_response_json("/geo/rdrp/paged?page=2&perPage=5")
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

def test_geo_run_filter():
    single_run = get_response_json("/geo/rdrp/paged?run=DRR021440")
    assert single_run['result'][0]['run_id'] == 'DRR021440'

    multiple_runs = get_response_json("/geo/rdrp/paged?run=DRR021440,SRR13187411")
    assert multiple_runs['result'][0]['run_id'] == 'DRR021440'
    assert multiple_runs['result'][1]['run_id'] == 'SRR13187411'
