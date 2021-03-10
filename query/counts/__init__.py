from flask_sqlalchemy_caching import FromCache
from application import cache

def get_counts(table, filter_col_value):
    filter_col = getattr(table, table.filter_col_name)
    select_column_names = ['score', 'percent_identity', 'count']
    select_columns = [getattr(table, name) for name in select_column_names]
    query = (table.query
        .filter(filter_col == filter_col_value)
        .with_entities(*select_columns)
        .options(FromCache(cache)))
    counts = query.all()
    result_json = [entry._asdict() for entry in counts]
    return result_json
