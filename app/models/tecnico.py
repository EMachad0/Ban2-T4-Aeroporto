from app.app import db


class Tecnico(db.Model):
    id_fun = db.Column(db.Integer, db.ForeignKey('tecnico.id_fun'), primary_key=True)
    endereco = db.Column(db.String(50))
    telefone = db.Column(db.Integer)
    salario = db.Column(db.Float, nullable=False)
