from app.app import db
from app.models import Tecnico, Funcionario


def get_all():
    return db.session.query(Tecnico.id_fun, Tecnico.endereco, Tecnico.telefone, Tecnico.salario,
                            Funcionario.n_matricula, Funcionario.n_membro) \
        .join(Funcionario, Tecnico.id_fun == Funcionario.id_fun) \
        .order_by(Funcionario.id_fun).all()


def insert(id_fun, endereco, telefone, salario, n_matricula, n_membro):
    db.session.execute(db.func.insert_tecnico(n_matricula, n_membro, endereco, telefone, salario, id_fun))
    db.session.commit()
