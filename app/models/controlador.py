from app.app import db


class Controlador(db.Document):
    data_exame = db.DateTimeField()
    n_matricula = db.IntField()
    n_membro = db.IntField()
