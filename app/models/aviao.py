from app.app import db


class Aviao(db.Model):
    id_avi = db.Column(db.Integer, primary_key=True)
    id_mod = db.Column(db.Integer, db.ForeignKey('modelo.id_mod'))
    n_registro = db.Column(db.Integer)
