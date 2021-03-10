from dataclasses import dataclass
from .. import db


@dataclass
class nfamily_counts(db.Model):
    family_name : str
    score : int
    percent_identity : int
    count : int

    family_name = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)

    filter_col_name = 'family_name'


@dataclass
class nsequence_counts(db.Model):
    genbank_id : str
    score : int
    percent_identity : int
    count : int

    genbank_id = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)

    filter_col_name = 'genbank_id'


@dataclass
class nfamily_list(db.Model):
    family_name : str
    family_name = db.Column(db.Text, primary_key=True)
    filter_col_name = 'family_name'


@dataclass
class nsequence_list(db.Model):
    genbank_id : str
    genbank_id = db.Column(db.Text, primary_key=True)
    filter_col_name = 'genbank_id'
