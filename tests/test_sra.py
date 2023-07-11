from . import get_response_json

def test_analysis_index_route():
    result = get_response_json("/index/run=ERR2756788")

    for [key, type] in [
        ['assembly_file', str],
        ['assembly', bool],
        ['geo', bool],
        ['micro', bool],
        ['nsra', bool],
        ['psra', bool],
        ['rsra', bool],
        ['run_id', str],
        ['srarun', bool]
    ]:
      assert key in result[0]
      assert isinstance(result[0][key], type)
