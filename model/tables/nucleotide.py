from dataclasses import dataclass
from .. import db

@dataclass
class nsra(db.Model):
    run_id : str
    read_length : int
    genome : str
    version : str
    date : str

    run_id = db.Column(db.Text, primary_key=True)
    read_length = db.Column(db.Integer)
    genome = db.Column(db.Text)
    version = db.Column(db.Text)
    date = db.Column(db.Text)


@dataclass
class nfamily(db.Model):
    run_id : str
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

    run_id = db.Column(db.Text, primary_key=True)
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

    filter_col_name = 'family_name'


@dataclass
class nsequence(db.Model):
    run_id : str
    family_name : str
    sequence_accession : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    n_global_reads : int
    length : int
    virus_name : str

    run_id = db.Column(db.Text, primary_key=True)
    family_name = db.Column(db.Text, primary_key=True)
    sequence_accession = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    n_global_reads = db.Column(db.Integer)
    length = db.Column(db.Integer)
    virus_name = db.Column(db.Text)

    filter_col_name = 'sequence_accession'
