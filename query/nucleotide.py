from .base import QueryBase
from model.tables.nucleotide import (
    nsra,
    nfamily,
    nsequence,
)
from model.views.nucleotide import (
    nfamily_counts,
    nsequence_counts,
    nfamily_list,
    nsequence_list,
)


class NucleotideQuery(QueryBase):
    def __init__(self):
        self.summary_table_map = {
            'properties': nsra,
            'families': nfamily,
            'sequences': nsequence
        }
        # url param key : table model
        self.table_map = {
            'family': nfamily,
            'sequence': nsequence
        }
        self.count_table_map = {
            'family': nfamily_counts,
            'sequence': nsequence_counts
        }
        self.list_table_map = {
            'family': nfamily_list,
            'sequence': nsequence_list
        }
