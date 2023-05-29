from model.tables.sra import (
    srarun
)
from model.tables.tax import (
    tax_lineage
)
from model import db

def get_host_rdrp_paginated(page=1, perPage=100, runIds=''):
    select_columns = [
        srarun.run.label('srarun.run'),
        srarun.tax_id.label('srarun.tax_id'),
        srarun.scientific_name.label('srarun.scientific_name'),
        tax_lineage.tax_id.label('tax_lineage.tax_id'),
        tax_lineage.tax_phylum.label('tax_lineage.tax_phylum'),
        tax_lineage.tax_order.label('tax_lineage.tax_order')
    ]
    filters = []
    if runIds:
        filters.append(srarun.run.in_(runIds))

    query = (
        srarun.query
            .with_entities(*select_columns)
            .join(tax_lineage, db.func.cast(srarun.tax_id, db.Integer) == tax_lineage.tax_id, isouter=True)
            .filter(*filters)
            .distinct(srarun.run)
            .distinct(srarun.tax_id)
    )
    pagination = query.paginate(page=int(page), per_page=int(perPage))
    pagination.items = [entry._asdict() for entry in pagination.items]
    return pagination
