from app.app import db


class Pericia(db.Model):
    id_mod = db.Column(db.Integer, db.ForeignKey('modelo.id_mod'), primary_key=True)
    id_fun = db.Column(db.Integer, db.ForeignKey('tecnico.id_fun'), primary_key=True)
