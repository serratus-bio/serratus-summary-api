from . import get_response_data


def test_analysis_index_route():
    data = get_response_data("/index/run=ERR2756788")
    assert data == {'run_id': 'ERR2756788', 'srarun': True, 'nsra': True, 'psra': True, 'rsra': True, 'assembly': True, 'micro': True, 'geo': False}
