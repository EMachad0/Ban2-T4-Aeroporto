from flask import Blueprint, redirect, render_template

from app.dao import teste_dao, tipo_teste_dao
from app.forms import TesteForm, TipoTesteForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('teste', __name__, static_folder="static", template_folder="templates")


@blue.route('/teste', methods=['GET', 'POST'])
def teste():
    form1 = TesteForm()
    if form1.validate_on_submit():
        teste_dao.insert(**remove_csrf(form1.data))
        return redirect('/teste')

    form2 = TipoTesteForm()
    if form2.validate_on_submit():
        tipo_teste_dao.insert(**remove_csrf(form2.data))
        return redirect('/teste')

    rows = teste_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Testes', table=table, forms=[form1, form2])
