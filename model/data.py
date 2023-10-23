from flask import current_app
from sqlalchemy import BigInteger, Column, Float, Text, create_engine
from sqlalchemy.orm import declarative_base

SQLAlchemyEngine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], echo=False)

Base = declarative_base()

type_to_sqlalchemy_type = {
    'bigint':BigInteger,
    # no Double in SQLAlchemy v1.4 :|
    'double precision':Float,
    'text':Text
}

# no auto-primary_keys due to permissions (?)
def model_from_table(name, __tablename__=None, columns=None, primary_keys=None):
    if(__tablename__ is None):
        __tablename__ = name

    if(columns is None):
        connection = SQLAlchemyEngine.connect()
        stmt = 'SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = \'public\' AND table_name = \'' + __tablename__ + '\' ORDER BY ordinal_position ASC;'
        columns = connection.execute(stmt).all()

        if(len(columns) == 0):
            # try a materialized view
            stmt = 'SELECT attname AS column_name, format_type(atttypid, atttypmod) AS data_type FROM pg_attribute WHERE attrelid = \'' + __tablename__ + '\'::regclass AND attnum > 0;'
            columns = connection.execute(stmt).all()
        
        connection.close()

    for key, value in columns:
        if value not in type_to_sqlalchemy_type:
            print('Missing sqlalchemy_type for \'' + value + '\'')

    sqlalchemy_columns = { key:type_to_sqlalchemy_type[value] if value in type_to_sqlalchemy_type else None for key, value in columns }
    sqlalchemy_columns = { key:Column(value, primary_key=primary_keys is not None and key in primary_keys) for key, value in sqlalchemy_columns.items() if value is not None }

    return type(name, (Base,), { **{ '__columns__':dict(columns), '__tablename__':__tablename__ }, **sqlalchemy_columns })
