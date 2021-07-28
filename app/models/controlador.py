from app.app import db


class Controlador(db.Model):
    id_fun = db.Column(db.Integer, db.ForeignKey('funcionario.id_fun'), primary_key=True)
    data_exame = db.Column(db.Date)
