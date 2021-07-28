from app.app import db


class Teste(db.Model):
    id_tes = db.Column(db.Integer, primary_key=True)
    id_avi = db.Column(db.Integer, db.ForeignKey('aviao.id_avi'))
    id_fun = db.Column(db.Integer, db.ForeignKey('tecnico.id_fun'))
    id_tit = db.Column(db.Integer, db.ForeignKey('tipoteste.id_tit'))
    data_teste = db.Column(db.Date)
    horas_gastas = db.Column(db.Integer)
    pontuacao = db.Column(db.Integer)
