from . import get_response_json

def test_list():
    values_list = get_response_json("/palmprint/run=ERR2756788")
    assert len(values_list) == 6