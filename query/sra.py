from .base import QueryBase
from model.tables.sra import (
    analysis_index,
)
from model.views.sra import (
    analysis_list,
)


class SraQuery(QueryBase):
    def __init__(self):
        self.summary_table_map = {
            'properties': analysis_index,
            'srarun_exists': srarun,
            'nsra_exists': nsra,
            'psra_exists': psra,
            'rsra_exists': rsra,
            'assembly_exists': assembly,
            'micro_exists': micro,
            'geo_exists': geo
        }