from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Modelo


def insert(**kwargs):
    ins = postgresql.insert(Modelo).values(kwargs).on_conflict_do_update(index_elements=[Modelo.id_mod], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
