from flask import jsonify, request, Response
from flask import current_app as app
from query.nucleotide import (
    get_matches_file,
    get_matches_paginated,
)


@app.route('/matches/nucleotide')
def get_matches_route():
    contents = get_matches_file(**request.args)
    filename = 'SerratusMatches.csv'
    headers = {'Content-Disposition': f'attachment;filename={filename}'}
    return Response(contents,
                    mimetype='text/csv',
                    headers=headers)


@app.route('/matches/nucleotide/paged')
def get_matches_paginated_route():
    pagination = get_matches_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
