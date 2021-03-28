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
    sequence_accession : str
    score : int
    percent_identity : int
    count : int

    sequence_accession = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)

    filter_col_name = 'sequence_accession'


@dataclass
class nfamily_list(db.Model):
    family_name : str
    family_name = db.Column(db.Text, primary_key=True)
    filter_col_name = 'family_name'


@dataclass
class nsequence_list(db.Model):
    sequence_accession : str
    virus_name : str
    sequence_accession = db.Column(db.Text, primary_key=True)
    virus_name = db.Column(db.Text)
    filter_col_name = 'sequence_accession'
