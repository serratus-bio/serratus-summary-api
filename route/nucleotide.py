from flask import jsonify, request, Response
from flask import current_app as app
from query import nucleotide_query
from application import cache


@app.route('/matches/nucleotide/download')
def get_matches_download_route():
    contents = nucleotide_query.get_matches_file(**request.args)
    filename = 'SerratusMatches.csv'
    headers = {'Content-Disposition': f'attachment;filename={filename}'}
    return Response(contents,
                    mimetype='text/csv',
                    headers=headers)

@app.route('/matches/nucleotide')
@cache.cached(query_string=True)
def get_matches_route():
    result = nucleotide_query.get_matches(**request.args)
    return jsonify(result)

@app.route('/matches/nucleotide/run/paged')
@cache.cached(query_string=True)
def get_run_matches_paginated_route():
    pagination = nucleotide_query.get_run_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)

@app.route('/matches/nucleotide/paged')
@cache.cached(query_string=True)
def get_matches_paginated_route():
    pagination = nucleotide_query.get_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)

@app.route('/counts/nucleotide')
@cache.cached(query_string=True)
def get_counts_route():
    counts = nucleotide_query.get_counts(**request.args)
    return jsonify(counts)

@app.route('/list/nucleotide/<query_type>')
@cache.cached(query_string=True)
def get_list_route(query_type):
    values_list = nucleotide_query.get_list(query_type, **request.args)
    return jsonify(values_list)
