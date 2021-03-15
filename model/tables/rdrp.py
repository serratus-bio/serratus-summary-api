from dataclasses import dataclass
from .. import db

@dataclass
class rsra(db.Model):
    run_id : str
    read_length : int
    genome : str
    aligned_reads : int
    date : str
    truncated : str

    run_id = db.Column(db.Text, primary_key=True)
    read_length = db.Column(db.Integer)
    genome = db.Column(db.Text)
    aligned_reads = db.Column(db.Integer)
    date = db.Column(db.Text)
    truncated = db.Column(db.Text)


@dataclass
class rphylum(db.Model):
    run_id : str
    phylum_name : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    aligned_length : int

    run_id = db.Column(db.Text, primary_key=True)
    phylum_name = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    aligned_length = db.Column(db.Integer)

    filter_col_name = 'phylum_name'


@dataclass
class rfamily(db.Model):
    run_id : str
    phylum_name : str
    family_name : str
    family_group : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    aligned_length : int

    run_id = db.Column(db.Text, primary_key=True)
    phylum_name = db.Column(db.Text, primary_key=True)
    family_name = db.Column(db.Text)
    family_group = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    aligned_length = db.Column(db.Integer)

    filter_col_name = 'family_name'


@dataclass
class rdrp(db.Model):
    run_id : str
    phylum_name : str
    family_name : str
    family_group : str
    virus_name : str
    sequence_accession : str
    coverage_bins : str
    score : int
    percent_identity : int
    depth : float
    n_reads : int
    aligned_length : int

    run_id = db.Column(db.Text, primary_key=True)
    phylum_name = db.Column(db.Text, primary_key=True)
    family_name = db.Column(db.Text)
    family_group = db.Column(db.Text, primary_key=True)
    virus_name = db.Column(db.Text, primary_key=True)
    sequence_accession = db.Column(db.Text, primary_key=True)
    coverage_bins = db.Column(db.Text)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    depth = db.Column(db.Float)
    n_reads = db.Column(db.Integer)
    aligned_length = db.Column(db.Integer)

    filter_col_name = 'sequence_accession'
