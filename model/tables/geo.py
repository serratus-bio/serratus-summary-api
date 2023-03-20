from dataclasses import dataclass
from .. import db


@dataclass
class rdrp_pos(db.Model):
    run_id = db.Column(db.Text, primary_key=True)
