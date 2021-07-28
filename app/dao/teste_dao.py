from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Teste, TipoTeste


def get_all():
    return db.session.query(Teste.id_tes, Teste.id_avi, Teste.id_fun, Teste.id_tit, Teste.data_teste, Teste.horas_gastas,
                            Teste.pontuacao, TipoTeste.n_anac, TipoTeste.nome, TipoTeste.pontuacao_maxima) \
        .join(TipoTeste, Teste.id_tit == TipoTeste.id_tit, full=True) \
        .order_by(Teste.id_tes, Teste.id_tit, Teste.pontuacao, TipoTeste.pontuacao_maxima).all()


def insert(**kwargs):
    ins = postgresql.insert(Teste).values(kwargs).on_conflict_do_update(index_elements=[Teste.id_tes], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
