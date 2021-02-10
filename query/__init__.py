def apply_filters(query, model, scoreMin=None, scoreMax=None, identityMin=None, identityMax=None):
    if scoreMin:
        query = query.filter(model.score >= int(scoreMin))
    if scoreMax:
        query = query.filter(model.score <= int(scoreMax))
    if identityMin:
        query = query.filter(model.percent_identity >= int(identityMin))
    if identityMax:
        query = query.filter(model.percent_identity <= int(identityMax))
    return query
