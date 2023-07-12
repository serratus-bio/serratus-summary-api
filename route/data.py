from flask import current_app, jsonify, request
from flask_caching import Cache
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, attributes, sessionmaker

import time


# A SINGLE ROUTE TO RULE THEM ALL !!!
# 
#                  ,#####,
#                  #_   _#
#                  |a` `a|
#                  |  u  |
#                  \  =  /
#                  |\___/|
#         ___ ____/:     :\____ ___
#       .'   `.-===-\   /-===-.`   '.
#      /      .-"""""-.-"""""-.      \
#     /'             =:=             '\
#   .'  ' .:    o   -=:=-   o    :. '  `.
#   (.'   /'. '-.....-'-.....-' .'\   '.)
#   /' ._/   ".     --:--     ."   \_. '\
#  |  .'|      ".  ---:---  ."      |'.  | 
#  |  : |       |  ---:---  |       | :  |
#   \ : |       |_____._____|       | : /
#   /   (       |----|------|       )   \
#  /... .|      |    |      |      |. ...\
# |::::/''     /     |       \     ''\::::|
# '""""       /'    .L_      `\       """"'
#            /'-.,__/` `\__..-'\
#           ;      /     \      ;
#           :     /       \     |
#           |    /         \.   |
#           |`../           |  ,/
#           ( _ )           |  _)
#           |   |           |   |
#           |___|           \___|
#           :===|            |==|
#            \  /            |__|
#            /\/\           /"""`8.__
#            |oo|           \__.//___)
#            |==|
#            \__/


# INIT
SQLAlchemyEngine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
SQLAlchemySession = sessionmaker(bind=SQLAlchemyEngine)()
auth = HTTPBasicAuth()
cache = Cache(current_app)

users = { 'serratus': 'serratus' }

@auth.verify_password
def verify_password(username, password):
    if(username in users and password == users[username]):
        return username


# MODELS
from model.data import model_from_table

model_dict = {
    'rfamily': model_from_table(name='rfamily', primary_keys=('run_id')),
    'rphylum': model_from_table(name='rphylum', primary_keys=('run_id')),
    'rsequence': model_from_table(name='rsequence', primary_keys=('run_id'))
}


# FUNCTIONS
def list_attributes_of_model(model):
    return list(filter(lambda x: isinstance(x, attributes.InstrumentedAttribute), model.__dict__.values()))

def data_query(arguments):
    # DEFAULT ARGUMENTS
    if('limit' not in arguments):
        arguments['limit'] = 8
    if('offset' not in arguments):
        arguments['offset'] = 0
    
    if('run_id' not in arguments):
        arguments['run_id'] = None
    if(isinstance(arguments['run_id'], str)):
        arguments['run_id'] = [arguments['run_id']]
    data_query = (
        SQLAlchemySession
            .query(arguments['view'])
            .with_entities(*list_attributes_of_model(arguments['view']))
    )
    
    # .where
    if(isinstance(arguments['run_id'], list)):
        data_query = (
            data_query
                .where(arguments['view'].run_id.in_(arguments['run_id']))
        )

    return (
        data_query
            .offset(arguments['offset'])
            .limit(arguments['limit'])
            .all()
    )


# ROUTE
@current_app.route('/data/cache/clear', methods=['GET'])
@auth.login_required
def GET_data_cache_clear():
    cache.clear()

    return 'true', 200

@current_app.route('/data/<view>', methods=['GET'])
@auth.login_required
def GET_data_view(view):
    request.args = dict(request.args)

    if('view' in request.args):
        view = request.args['view']

    if(view is None):
        return jsonify(error='Missing parameter in URL: view'), 400
    
    if(view in model_dict):
        view = request.args['view'] = model_dict[view]
    else:
        return jsonify(error='Invalid parameter in URL: view \'' + view + '\' not found'), 400
    
    for key, value in request.args.items():
        if(isinstance(value, str) and ',' in value):
            request.args[key] = value.split(',')
    
    if(cache.get(request.full_path) == None):
        _data_query = data_query({ 'view':view } | request.args)

        cache.set(request.full_path, _data_query)
    else:
        _data_query = cache.get(request.full_path)

    return jsonify(data=[row._asdict() for row in _data_query]), 200

@current_app.route('/data/<view>', methods=['POST'])
@auth.login_required
def POST_data_view(view):
    json = None
    try:
        json = request.json
    except:
        pass
    
    if(json is None):
        return jsonify(error='Empty or invalid JSON payload'), 400

    if('view' in json):
        view = json['view']

    if(view is None):
        return jsonify(error='Missing parameter in URL: view'), 400
    
    if(view in model_dict):
        view = model_dict[view]
    else:
        return jsonify(error='Invalid parameter in URL: view \'' + view + '\' not found'), 400
    
    _data_query = data_query({ 'view':view } | json)

    return jsonify(data=[row._asdict() for row in _data_query]), 200
