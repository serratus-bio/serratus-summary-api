from model.tables.sra import (
    srarun,
)
from model.tables.geo import (
    rdrp_pos,
)
from model.views.geo import (
    srarun_geo_coordinates,
)


def get_geo_rdrp_paginated(page=1, perPage=500, run=''):
    select_columns = [
        srarun_geo_coordinates.run_id,
        srarun_geo_coordinates.biosample_id,
        srarun.release_date,
        srarun.tax_id,
        srarun.scientific_name,
        srarun_geo_coordinates.coordinate_x,
        srarun_geo_coordinates.coordinate_y,
        srarun_geo_coordinates.from_text
    ]
    filters = []
    if run:
        filters.append(srarun_geo_coordinates.run_id.in_(run.split(',')))

    query = (
        srarun_geo_coordinates.query
        .with_entities(*select_columns)
        .join(rdrp_pos, srarun_geo_coordinates.run_id == rdrp_pos.run_id)
        .join(srarun, srarun_geo_coordinates.run_id == srarun.run)
        .filter(*filters)
        .distinct(srarun_geo_coordinates.run_id)
        .order_by(srarun_geo_coordinates.run_id))
    pagination = query.paginate(page=int(page), per_page=int(perPage))
    pagination.items = [entry._asdict() for entry in pagination.items]
    return pagination
