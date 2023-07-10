from . import  get_response_json

def test_paginate_geo():
    first_page = get_response_json("/geo/rdrp/paged?page=1&perPage=10")
    assert len(first_page['result']) == 10
    
    assert 'run_id' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['run_id'], str)
    assert 'biosample_id' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['biosample_id'], str)
    assert 'release_date' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['release_date'], str)
    assert 'tax_id' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['tax_id'], str)
    assert 'scientific_name' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['scientific_name'], str)
    assert 'coordinate_x' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['coordinate_x'], float)
    assert 'coordinate_y' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['coordinate_y'], float)
    assert 'from_text' in first_page['result'][0]
    assert isinstance(first_page['result'][0]['from_text'], str)

    second_page = get_response_json("/geo/rdrp/paged?page=2&perPage=5")
    
    assert first_page['result'][5] == second_page['result'][0]
    assert first_page['result'][6] == second_page['result'][1]
    assert first_page['result'][7] == second_page['result'][2]
    assert first_page['result'][8] == second_page['result'][3]
    assert first_page['result'][9] == second_page['result'][4]

# def test_geo_run_filter():
#     expected = {
#           "DRR021440" : {
#             "run_id":	"DRR021440",
#             "biosample_id":	"SAMD00018407",
#             "release_date":	"Tue, 14 Jul 2015 10:38:15 GMT",
#             "tax_id":	"318829",
#             "scientific_name":	"Pyricularia oryzae",
#             "coordinate_x":	-53.073466889,
#             "coordinate_y":	-10.769946429,
#             "from_text":	"brazil",
#           },
#         "SRR13187411": {
#             "run_id":	"SRR13187411",
#             "biosample_id":	"SAMN16984707",
#             "release_date":	"Wed, 02 Dec 2020 19:04:46 GMT",
#             "tax_id":	"2697049",
#             "scientific_name":	"Severe acute respiratory syndrome coronavirus 2",
#             "coordinate_x":	-91.0969,
#             "coordinate_y":	30.5694,
#             "from_text":	None
#         }
#     }

#     single_run = get_response_json("/geo/rdrp/paged?run=DRR021440")
#     assert single_run['result'][0] == expected['DRR021440']

#     multiple_runs = get_response_json("/geo/rdrp/paged?run=DRR021440,SRR13187411")
#     assert multiple_runs['result'][0] == expected['DRR021440']
#     assert multiple_runs['result'][1] == expected['SRR13187411']
