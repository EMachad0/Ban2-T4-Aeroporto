from flask import Blueprint, redirect, render_template
from flask_mongoengine.wtf import model_form

from app.dao import teste_dao
from app.models import Teste, Aviao
from app.forms import TesteForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('teste', __name__, static_folder="static", template_folder="templates")


@blue.route('/teste', methods=['GET', 'POST'])
def teste():
    form = TesteForm()
    if form.validate_on_submit():
        print(form.data, flush=True)
        teste_dao.insert(**remove_csrf(form.data))
        return redirect('/teste')

    rows = teste_dao.get_all()
    table = [
        {'Avião': {'Nº registro': row.aviao.n_registro},
         'Técnico': {'Nº membro': row.tecnico.n_membro},
         'TipoTeste': {'Nº ANAC': row.tipo_teste.n_anac},
         'Horas Gastas': row.horas_gastas,
         'Pontuação': row.pontuacao} for row in rows]
    print(table, flush=True)
    return render_template('page.html', title='Testes', table=table, forms=[form])
