from app.app import db


class Teste(db.Document):
    aviao = db.ReferenceField('Aviao', required=True)
    tecnico = db.ReferenceField('Tecnico', required=True)
    tipo_teste = db.ReferenceField('TipoTeste', required=True)
    data_teste = db.DateTimeField()
    horas_gastas = db.IntField()
    pontuacao = db.IntField()
