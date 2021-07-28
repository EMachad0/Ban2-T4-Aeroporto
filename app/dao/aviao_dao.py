from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Aviao, Modelo


def get_all():
    return db.session.query(Aviao.id_avi, Aviao.n_registro, Aviao.id_mod, Modelo.cod, Modelo.capacidade, Modelo.peso) \
        .join(Modelo, Aviao.id_mod == Modelo.id_mod, full=True) \
        .order_by(Aviao.id_mod, Modelo.id_mod).all()


def insert(**kwargs):
    ins = postgresql.insert(Aviao).values(kwargs).on_conflict_do_update(index_elements=[Aviao.id_avi], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
