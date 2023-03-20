from . import  get_response_json


def test_paginate_geo():
    rdrp_pos = get_response_json("/geo/rdrp/paged?page=1&perPage=10")
    assert len(rdrp_pos['result']) == 10
    assert rdrp_pos['result'][0] == {
      "run_id": "DRR021440",
      "biosample_id": "SAMD00018407",
      "release_date": "Tue, 14 Jul 2015 10:38:15 GMT",
      "tax_id": "318829",
      "scientific_name": "Pyricularia oryzae",
      "coordinate_x": -53.073466889,
      "coordinate_y": -10.769946429,
      "from_text": "brazil"
    }


    rdrp_pos = get_response_json("/geo/rdrp/paged?page=6&perPage=5")
    assert len(rdrp_pos['result']) == 5
    assert rdrp_pos['result'][0] == {
        "run_id":	"DRR029069",
        "biosample_id":	"SAMD00024757",
        "release_date":	"Mon, 26 Jan 2015 10:28:36 GMT",
        "tax_id":	"64793",
        "scientific_name":	"Wasmannia auropunctata",
        "coordinate_x":	-52.97901,
        "coordinate_y":	5.067,
        "from_text":	None,
    }
