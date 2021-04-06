from dataclasses import dataclass
from .. import db

@dataclass
class analysis_index(db.Model):
    run_id : str
    srarun : bool
    nsra : bool
    psra : bool
    rsra : bool
    assembly : bool
    micro : bool
    geo : bool

    run_id = db.Column(db.Text, primary_key=True)
    srarun = db.Column(db.Boolean)
    nsra = db.Column(db.Boolean)
    psra = db.Column(db.Boolean)
    rsra = db.Column(db.Boolean)
    assembly = db.Column(db.Boolean)
    micro = db.Column(db.Boolean)
    geo = db.Column(db.Boolean)

    filter_col_name = 'run_id'
