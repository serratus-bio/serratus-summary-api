from flask import jsonify, request
from flask import current_app as app
from query import get_geo_rdrp_paginated


@app.route('/geo/rdrp/paged')
def get_geo_rdrp_paginated_route():
    pagination = get_geo_rdrp_paginated(**request.args)
    total = pagination.total
    result = pagination.items
    return jsonify(result=result, total=total)
