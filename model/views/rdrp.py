from dataclasses import dataclass
from .. import db


@dataclass
class rphylum_counts(db.Model):
    phylum_name : str
    score : int
    percent_identity : int
    count : int

    phylum_name = db.Column(db.Text, primary_key=True)
    score = db.Column(db.Integer)
    percent_identity = db.Column(db.Integer)
    count = db.Column(db.Integer)

    filter_col_name = 'phylum_name'


@dataclass
class rfamily_counts(db.Model):
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
class rsequence_counts(db.Model):
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
class rphylum_list(db.Model):
    phylum_name : str
    phylum_name = db.Column(db.Text, primary_key=True)
    filter_col_name = 'phylum_name'


@dataclass
class rfamily_list(db.Model):
    family_name : str
    family_name = db.Column(db.Text, primary_key=True)
    filter_col_name = 'family_name'


@dataclass
class rsequence_list(db.Model):
    sequence_accession : str
    virus_name : str
    sequence_accession = db.Column(db.Text, primary_key=True)
    virus_name = db.Column(db.Text)
    filter_col_name = 'sequence_accession'

@dataclass
class srarun_geo_coordinates(db.Model):
    run_id = db.Column(db.Text, primary_key=True)
    biosample_id = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    coordinate_x = db.Column(db.Float)
    coordinate_y = db.Column(db.Float)
    from_text = db.Column(db.Text)

@dataclass
class rdrp_pos(db.Model):
    run_id = db.Column(db.Text, primary_key=True)


@dataclass
class srarun(db.Model):
    run = db.Column(db.Text, primary_key=True)
    release_date = db.Column(db.DateTime)
    tax_id = db.Column(db.Text)
    scientific_name = db.Column(db.Text)
