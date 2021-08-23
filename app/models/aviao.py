from app.app import db
from app.models.modelo import Modelo


class Aviao(db.Document):
    n_registro = db.IntField()
    modelo = db.EmbeddedDocumentField(Modelo)
