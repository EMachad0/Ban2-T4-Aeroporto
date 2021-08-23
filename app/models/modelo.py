from app.app import db


class Modelo(db.EmbeddedDocument):
    cod = db.StringField(max_length=10)
    capacidade = db.IntField(required=True)
    peso = db.IntField(required=True)
