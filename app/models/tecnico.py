from app.app import db
from app.models.modelo import Modelo


class Tecnico(db.Document):
    endereco = db.StringField(max_length=50)
    telefone = db.IntField()
    salario = db.FloatField(required=True)
    n_matricula = db.IntField(required=True)
    n_membro = db.IntField(required=True)
    pericias = db.EmbeddedDocumentListField(Modelo)
