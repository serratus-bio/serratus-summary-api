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
    srarun_geo_coordinates,
    rdrp_pos,
    srarun,
)
from model import db


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

    def query_srarun_geo_coordnates(self, page, perPage):
        query = db.session.query(srarun_geo_coordinates.run_id, srarun_geo_coordinates.biosample_id, srarun.release_date, srarun.tax_id,
                 srarun.scientific_name, srarun_geo_coordinates.coordinate_x, srarun_geo_coordinates.coordinate_y,
                 srarun_geo_coordinates.from_text)\
                .join(rdrp_pos, srarun_geo_coordinates.run_id == rdrp_pos.run_id)\
                .join(srarun, srarun_geo_coordinates.run_id == srarun.run)\
                .distinct(srarun_geo_coordinates.run_id)\
                .order_by(srarun_geo_coordinates.run_id)
        return query.paginate(page=int(page), per_page=int(perPage))
