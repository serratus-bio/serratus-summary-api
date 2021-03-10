from dataclasses import dataclass
from .. import db


@dataclass
class nfamily_counts(db.Model):
    family_name : str
    score : int
    percent_identity : int
    count : int

    filter_col_name = 'family_name'

    family_name = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)


@dataclass
class nsequence_counts(db.Model):
    genbank_id : str
    score : int
    percent_identity : int
    count : int

    filter_col_name = 'genbank_id'

    genbank_id = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)


@dataclass
class nfamily_list(db.Model):
    family_name : str

    filter_col_name = 'family_name'

    family_name = db.Column(db.Text, primary_key=True)


@dataclass
class nsequence_list(db.Model):
    genbank_id : str

    filter_col_name = 'genbank_id'

    genbank_id = db.Column(db.Text, primary_key=True)
