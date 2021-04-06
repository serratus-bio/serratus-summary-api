from .base import QueryBase
from model.views.sra import analysis_index

def get_analysis_index(run_id):
    query = analysis_index.query.filter(analysis_index.run_id == run_id)
    return query.one()
