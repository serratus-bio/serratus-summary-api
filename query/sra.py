from .base import QueryBase
from model.tables.sra import (
    analysis_index,
)
from model.views.sra import (
    analysis_list,
)


class SraQuery(QueryBase):
    def __init__(self):
        self.index_table_map = {
            'analysis_index': analysis_index,
        }

