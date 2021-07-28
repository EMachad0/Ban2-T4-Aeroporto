from app.app import db
from app.models import Controlador, Funcionario


def get_all():
    return db.session.query(Controlador.id_fun, Controlador.data_exame, Funcionario.n_matricula, Funcionario.n_membro) \
        .join(Funcionario, Controlador.id_fun == Funcionario.id_fun) \
        .order_by(Funcionario.id_fun).all()


def insert(id_fun, n_matricula, n_membro, data_exame):
    db.session.execute(db.func.insert_controlador(n_matricula, n_membro, data_exame, id_fun))
    db.session.commit()
