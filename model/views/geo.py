from dataclasses import dataclass
from .. import db


@dataclass
class srarun_geo_coordinates(db.Model):
    run_id = db.Column(db.Text, primary_key=True)
    biosample_id = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    coordinate_x = db.Column(db.Float)
    coordinate_y = db.Column(db.Float)
    from_text = db.Column(db.Text)
