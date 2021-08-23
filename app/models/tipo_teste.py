from app.app import db


class TipoTeste(db.Document):
    n_anac = db.IntField()
    nome = db.StringField(max_length=50)
    pontuacao_maxima = db.IntField()
