from application import cache
from flask import current_app as app
from flask import jsonify, request
from json import dumps
from query import get_host_rdrp_paginated

@app.route('/host/rdrp/paged', methods=['GET', 'POST'])
@cache.cached(query_string=True, unless=lambda: request.method != 'GET')
def get_host_rdrp_paginated_route():
    print('get_host_rdrp_paginated_route: ' + request.method)

    if request.method == 'GET':
        args = request.args.to_dict()
        if 'runIds' in args:
            args['runIds'] = args['runIds'].split(',')
    elif request.method == 'POST':
        args = request.get_json()

    pagination = get_host_rdrp_paginated(**args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
