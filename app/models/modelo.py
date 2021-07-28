from app.app import db


class Modelo(db.Model):
    id_mod = db.Column(db.Integer, primary_key=True)
    cod = db.Column(db.Integer)
    capacidade = db.Column(db.Integer)
    peso = db.Column(db.Integer)
