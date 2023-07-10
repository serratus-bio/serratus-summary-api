from sqlalchemy import Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class rfamily(Base):
    __tablename__  = 'rfamily'

    run_id = Column(Text, primary_key=True)
    phylum_name = Column(Text, primary_key=True)

class rphylum(Base):
    __tablename__  = 'rphylum'

    run_id = Column(Text, primary_key=True)
    phylum_name = Column(Text, primary_key=True)

class rsequence(Base):
    __tablename__  = 'rsequence'

    run_id = Column(Text, primary_key=True)
    phylum_name = Column(Text, primary_key=True)
