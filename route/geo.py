from flask import jsonify, request
from flask import current_app as app
from query import get_geo_rdrp_paginated
from application import cache


@app.route('/geo/rdrp/paged')
@cache.cached(query_string=True)
def get_geo_rdrp_paginated_route():
    pagination = get_geo_rdrp_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
