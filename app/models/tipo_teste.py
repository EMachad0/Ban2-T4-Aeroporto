from app.app import db


class TipoTeste(db.Model):
    __tablename__ = 'tipo_teste'
    id_tit = db.Column(db.Integer, primary_key=True)
    n_anac = db.Column(db.Integer)
    nome = db.Column(db.String(50))
    pontuacao_maxima = db.Column(db.Integer)
