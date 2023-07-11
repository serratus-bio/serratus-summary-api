from flask import current_app, jsonify, request
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, attributes, sessionmaker


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
SQLAlchemyEngine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
SQLAlchemySession = sessionmaker(bind=SQLAlchemyEngine)()
auth = HTTPBasicAuth()

users = { 'serratus': 'serratus' }

@auth.verify_password
def verify_password(username, password):
    if(username in users and password == users[username]):
        return username


# MODELS
from model.data import rfamily
from model.data import rphylum
from model.data import rsequence

model_dict = {
    'rfamily': rfamily,
    'rphylum': rphylum,
    'rsequence': rsequence
}

# FUNCTIONS
def list_attributes_of_model(model):
    return list(filter(lambda x: isinstance(x, attributes.InstrumentedAttribute), model.__dict__.values()))


# ROUTE
@current_app.route('/data', methods=['POST'])
@auth.login_required
def get_data():
    json = None
    try:
        json = request.json
    except:
        print('err')
    
    if(json is None):
        return jsonify(error='Empty or invalid JSON payload'), 400

    view = None
    if('view' in json):
        view = json['view']

    if(view is None):
        return jsonify(error='Missing parameter in JSON payload: view'), 400
    
    if(view in model_dict):
        view = model_dict[view]
    else:
        return jsonify(error='Invalid parameter in JSON payload: view \'' + view + '\' not found'), 400
    
    # DEFAULT REQUEST PARAMETERS
    if('run_id' not in json):
        json['run_id'] = None
    
    if(isinstance(json['run_id'], str)):
        json['run_id'] = [json['run_id']]
    
    query = (
        SQLAlchemySession
            .query(view)
            .with_entities(*list_attributes_of_model(view))
    )
    
    # .where
    if(isinstance(json['run_id'], list)):
        query = (
            query
                .where(view.run_id.in_(json['run_id']))
        )

    query = (
        query
            .limit(8)
            .all()
    )

    return jsonify(data=[row._asdict() for row in query]), 200
