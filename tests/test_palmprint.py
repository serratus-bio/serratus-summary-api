from . import get_response_json

def test_list():
    result = get_response_json("/palmprint/run=ERR2756788")

    for [key, type] in [
        ['assembly_node', int],
        ['cigar', str],
        ['coverage', float],
        ['evalue', float],
        ['palm_id', str],
        ['percent_identity', float],
        ['pp_end', int],
        ['pp_start', int],
        ['q_end', int],
        ['q_len', int],
        ['q_sequence', str],
        ['q_start', int],
        ['q_strand', str],
        ['qc_pass', bool],
        ['row_id', int],
        ['run_id', str]
    ]:
      assert key in result[0]
      assert isinstance(result[0][key], type)
