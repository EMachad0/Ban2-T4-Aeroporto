from app.app import db


class Funcionario(db.Model):
    id_fun = db.Column(db.Integer, primary_key=True)
    n_matricula = db.Column(db.Integer)
    n_membro = db.Column(db.Integer)
