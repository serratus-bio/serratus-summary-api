from flask import current_app, jsonify, request
from flask_caching import Cache
from flask_httpauth import HTTPBasicAuth
from hashlib import md5
from re import sub
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
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
SQLAlchemyEngine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], echo=True, max_overflow=32, pool_size=32)
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
    'dfamily': model_from_table(name='dfamily', primary_keys=('run_id')),
    'dphylum': model_from_table(name='dphylum', primary_keys=('run_id')),
    'dsequence': model_from_table(name='dsequence', primary_keys=('run_id')),
    'dsra': model_from_table(name='dsra', primary_keys=('run_id')),
    'rfamily': model_from_table(name='rfamily', primary_keys=('run_id')),
    # 'rfamily_counts': model_from_table(name='rfamily_counts', columns=[('family_name', 'text'), ('score', 'bigint'), ('percent_identity', 'bigint'), ('count', 'bigint')], primary_keys=('family_name')),
    'rfamily_counts': model_from_table(name='rfamily_counts', primary_keys=('family_name')),
    'rphylum': model_from_table(name='rphylum', primary_keys=('run_id')),
    'rsequence': model_from_table(name='rsequence', primary_keys=('run_id')),
    'rsra': model_from_table(name='rsra', primary_keys=('run_id')),
    'srarun': model_from_table(name='srarun', primary_keys=('run'))
}


# FUNCTIONS
def list_attributes_of_model(model):
    return list(filter(lambda x: isinstance(x, attributes.InstrumentedAttribute), model.__dict__.values()))

def data_query(arguments):
    # DEFAULT ARGUMENTS
    if('_limit' not in arguments):
        arguments['_limit'] = 8
    if('_offset' not in arguments):
        arguments['_offset'] = 0

    data_session = sessionmaker(bind=SQLAlchemyEngine)()

    data_entities = list_attributes_of_model(arguments['view'])
    if('_columns' in arguments):
        if(not isinstance(arguments['_columns'], list)):
            arguments['_columns'] = [arguments['_columns']]

        data_entities = list(map(lambda x: getattr(arguments['view'], x), filter(lambda x: hasattr(arguments['view'], x), arguments['_columns'])))

    data_query = (
        data_session
            .query(arguments['view'])
            .with_entities(*data_entities)
    )
    
    # .where
    for key in arguments['view'].__columns__:
        _key = str(key).split('.').pop();

        if(_key in arguments):
            if(not isinstance(arguments[_key], list)):
                arguments[_key] = [arguments[_key]]

            if(hasattr(arguments['view'], _key)):
                if(arguments['view'].__columns__[_key] in ['bigint', 'double precision']):
                    if(len(arguments[_key]) == 2):
                        if(not arguments[_key][0] == ''):
                            data_query = data_query.where(getattr(arguments['view'], _key) >= arguments[_key][0])
                        if(not arguments[_key][1] == ''):
                            data_query = data_query.where(getattr(arguments['view'], _key) <= arguments[_key][1])
                    else:
                        data_query = data_query.where(getattr(arguments['view'], _key).in_(arguments[_key]))

                if(arguments['view'].__columns__[_key] in ['text']):
                    data_query = data_query.where(getattr(arguments['view'], _key).in_(arguments[_key]))
    
    data_session.close()

    if('_count' in arguments):
        print('memoize query')
        stmt = 'SELECT count(*) as count_1 FROM(' + sub('\n', '', str(data_query.statement.compile(dialect=postgresql.dialect()))) + ') AS anon_1'
        stmt_md5 = md5(stmt.encode('utf-8')).hexdigest()
        print('-->', stmt, stmt_md5)

        # check if it's there
        # if it's not calculate and store
        # return value

        return (
            data_query
                .count()
        )
    else:
        if(arguments['_offset'] != '0'):
            data_query = data_query.offset(arguments['_offset'])
        if(arguments['_limit'] != '0'):
            data_query = data_query.limit(arguments['_limit'])
        
        return data_query.all()

def data_return(data):
    if(isinstance(data, int)):
        return jsonify(data=data), 200
    elif(isinstance(data, list)):
        return jsonify(data=[row._asdict() for row in data]), 200
    else:
        return jsonify(data={}), 200

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
        _data_query = data_query({ **{ 'view':view }, **request.args })

        cache.set(request.full_path, _data_query)
    else:
        _data_query = cache.get(request.full_path)
    
    return data_return(_data_query)

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
    
    _data_query = data_query({ **{ 'view':view }, **json })

    return data_return(_data_query)
