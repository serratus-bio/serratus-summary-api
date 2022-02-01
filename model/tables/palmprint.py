from dataclasses import dataclass
from sqlalchemy.orm import synonym
from .. import db

@dataclass
class palm_sra(db.Model):
    row_id : int
    run_id : str
    assembly_node : int
    coverage : float
    q_start : int
    q_end : int
    q_len : int
    q_strand : str
    palm_id : str
    pp_start : int
    pp_end : int
    percent_identity : float
    evalue : float
    cigar : str
    q_sequence : str
    qc_pass : bool

    row_id = db.Column(db.Integer, primary_key=True)
    run_id = db.Column(db.Text)
    assembly_node = db.Column(db.Integer)
    coverage = db.Column(db.Float)
    q_start = db.Column(db.Integer)
    q_end = db.Column(db.Integer)
    q_len = db.Column(db.Integer)
    q_strand = db.Column(db.String)
    palm_id = db.Column(db.Text)
    pp_start = db.Column(db.Integer)
    pp_end = db.Column(db.Integer)
    pp_len = db.Column(db.Integer)
    percent_identity = db.Column(db.Float)
    evalue = db.Column(db.Float)
    cigar = db.Column(db.Text)
    q_sequence = db.Column(db.Text)
    qc_pass = db.Column(db.Boolean)
