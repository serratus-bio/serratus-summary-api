from dataclasses import dataclass
from .. import db

@dataclass
class tax_lineage(db.Model):
    row_id = db.Column(db.Text, primary_key=True)
    tax_id = db.Column(db.Integer)
    tax_phylum = db.Column(db.Text)
    tax_order = db.Column(db.Text)
