from flask import jsonify, request, Response
from flask import current_app as app
from query import rdrp_query


@app.route('/matches/rdrp')
def get_rdrp_matches_route():
    contents = rdrp_query.get_matches_file(**request.args)
    filename = 'SerratusMatches.csv'
    headers = {'Content-Disposition': f'attachment;filename={filename}'}
    return Response(contents,
                    mimetype='text/csv',
                    headers=headers)

@app.route('/matches/rdrp/run/paged')
def get_rdrp_run_matches_paginated_route():
    pagination = rdrp_query.get_run_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)

@app.route('/matches/rdrp/paged')
def get_rdrp_matches_paginated_route():
    pagination = rdrp_query.get_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)

@app.route('/counts/rdrp')
def get_rdrp_counts_route():
    counts = rdrp_query.get_counts(**request.args)
    return jsonify(counts)

@app.route('/list/rdrp/<query_type>')
def get_rdrp_list_route(query_type):
    values_list = rdrp_query.get_list(query_type, **request.args)
    return jsonify(values_list)
