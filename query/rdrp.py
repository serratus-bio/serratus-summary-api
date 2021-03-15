from .base import QueryBase
from model.tables.rdrp import (
    rsra,
    rphylum,
    rfamily,
    rdrp,
)
from model.views.rdrp import (
    rphylum_counts,
    rfamily_counts,
    rdrp_counts,
    rphylum_list,
    rfamily_list,
    rdrp_list,
)


class RdrpQuery(QueryBase):
    def __init__(self):
        self.summary_table_map = {
            'properties': rsra,
            'phylums': rphylum,
            'families': rfamily,
            'sequences': rdrp
        }
        # url param key : table model
        self.table_map = {
            'phylum': rphylum,
            'family': rfamily,
            'sequence': rdrp
        }
        self.count_table_map = {
            'phylum': rphylum_counts,
            'family': rfamily_counts,
            'sequence': rdrp_counts
        }
        self.list_table_map = {
            'phylum': rphylum_list,
            'family': rfamily_list,
            'sequence': rdrp_list
        }
