from flask import jsonify, make_response, request, Response
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

@app.route('/pos/rdrp')
def get_rdrp_pos_route():
    """
    Function to return the rdrp_pos table data from the SQL server

    Returns:
        A JSON response containing the result of the query in the form of a list of dictionaries. If the page or perPage
        parameters are invalid, an error message is returned with a status code of 400.
    """
    if not request.args.get('page'):
        page = 1
    else:
        page = validate_args(request.args['page'])
    if not page:
        error = {'message': 'Invalid page parameter: {arg}'.format(arg = request.args['page'])}
        return make_response(jsonify(error), 400)

    if not request.args.get('perPage'):
        perPage = 20
    else:
        perPage = validate_args(request.args['perPage'])
    if not perPage:
        error = {'message': 'Invalid perPage parameter: {arg}'.format(arg = request.args['perPage'])}
        return make_response(jsonify(error), 400)

    pos = rdrp_query.query_srarun_geo_coordnates(page=page, perPage=perPage)
    result = pos.items
    column_names = ['run_id', 'biosample_id', 'release_date', 'tax_id', 'scientific_name', 'coordinate_x', 'coordinate_y', 'from_text']
    result = []
    for tuple_item in pos.items:
        record = {}
        for col_ind, value in enumerate(tuple_item):
            record.update({column_names[col_ind]: value})
        result.append(record)
    return jsonify(result=result)

def validate_args(param):
    """
    Function to validate an argument to ensure it is a positive integer.

    Arguments:
        param: The argument to validate.

    Returns:
        The integer representation of the argument if it is a positive integer, False otherwise.
    """
    try:
        int_param = int(param)
        if int_param > 0:
            return int_param
        else:
            return False
    except ValueError:
        return False
