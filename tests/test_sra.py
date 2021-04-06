import application
import json
from route.sra import get_index_run_route


def test_analysis_index_route():
    response = application.app.test_client().get("/index/run=ERR2756788")
    data = json.loads(response.get_data(as_text=True))
    assert data == {'run_id': 'ERR2756788', 'srarun': True, 'nsra': True, 'psra': True, 'rsra': True, 'assembly': True, 'micro': True, 'geo': False}
