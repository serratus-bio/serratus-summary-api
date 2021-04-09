from .base import QueryBase
from model.tables.rdrp import (
    rphylum,
    rfamily,
    rsequence,
)
from model.views.rdrp import (
    rphylum_counts,
    rfamily_counts,
    rsequence_counts,
    rphylum_list,
    rfamily_list,
    rsequence_list,
)


class RdrpQuery(QueryBase):
    def __init__(self):
        # url param key : table model
        self.table_map = {
            'phylum': rphylum,
            'family': rfamily,
            'sequence': rsequence
        }
        self.count_table_map = {
            'phylum': rphylum_counts,
            'family': rfamily_counts,
            'sequence': rsequence_counts
        }
        self.list_table_map = {
            'phylum': rphylum_list,
            'family': rfamily_list,
            'sequence': rsequence_list
        }
