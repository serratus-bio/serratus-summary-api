from . import get_counts
from model.views.nucleotide import (
    nfamily_counts,
    nsequence_counts,
)

count_table_map = {
    'family': nfamily_counts,
    'genbank': nsequence_counts
}

def get_count_table_key(**url_params):
    for key in count_table_map:
        if key in url_params:
            return key

def get_counts_from_params(**url_params):
    key = get_count_table_key(**url_params)
    table = count_table_map[key]
    filter_col_value = url_params.pop(key)
    return get_counts(table, filter_col_value)
