from dataclasses import dataclass
from .. import db

@dataclass
class analysis_list(db.Model):
    run_id : str
    srarun : str
    nsra : str
    psra : str
    rsra : str
    assembly : str
    micro : str
    geo : str

    run_id = db.Column(db.Text, primary_key=True)
    srarun = db.Column(db.Text)
    nsra = db.Column(db.Text)
    psra = db.Column(db.Text)
    rsra = db.Column(db.Text)
    assembly = db.Column(db.Text)
    micro = db.Column(db.Text)
    geo = db.Column(db.Text)

    filter_col_name = 'run_id'

