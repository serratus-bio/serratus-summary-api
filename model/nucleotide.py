from dataclasses import dataclass
from . import db

@dataclass
class nsra(db.Model):
    sra_id : str
    read_length : int
    genome : str
    version : str
    date : str

    sra_id = db.Column(db.Text, primary_key=True)
    read_length = db.Column(db.Integer)
    genome = db.Column(db.Text)
    version = db.Column(db.Text)
    date = db.Column(db.Text)


@dataclass
class nfamily(db.Model):
    sra_id : str
    family_name : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    n_global_reads : int
    length : int
    # top_genbank_id : str
    # top_score : int
    # top_length : int
    # top_name : str

    filter_col_name = 'family_name'

    sra_id = db.Column(db.Text, primary_key=True)
    family_name = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    n_global_reads = db.Column(db.Integer)
    length = db.Column(db.Integer)
    # top_genbank_id = db.Column(db.Text)
    # top_score = db.Column(db.Integer)
    # top_length = db.Column(db.Integer)
    # top_name = db.Column(db.Text)


@dataclass
class nsequence(db.Model):
    sra_id : str
    family_name : str
    genbank_id : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    n_global_reads : int
    length : int
    genbank_name : str

    filter_col_name = 'genbank_id'

    sra_id = db.Column(db.Text, primary_key=True)
    family_name = db.Column(db.Text, primary_key=True)
    genbank_id = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    n_global_reads = db.Column(db.Integer)
    length = db.Column(db.Integer)
    genbank_name = db.Column(db.Text)
