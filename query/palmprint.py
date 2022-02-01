from .base import QueryBase
from model.tables.palmprint import palm_sra

# select run_id, assembly_node, palm_id, percent_identity, evalue, coverage from palm_sra
# where run_id = 'ERR2756788'
# and qc_pass = true
# order by coverage desc

def get_palmprint(run_id):
    query = palm_sra.query.filter(palm_sra.run_id == run_id,
            palm_sra.qc_pass == True)
    query = query.order_by(palm_sra.coverage.desc())
    return query.all()

