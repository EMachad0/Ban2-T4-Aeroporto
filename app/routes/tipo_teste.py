from flask import Blueprint, redirect, render_template

from app.dao import tipo_teste_dao
from app.forms import TipoTesteForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('tipo_teste', __name__, static_folder="static", template_folder="templates")


@blue.route('/tipo_teste', methods=['GET', 'POST'])
def tipo_teste():
    form = TipoTesteForm()
    if form.validate_on_submit():
        tipo_teste_dao.insert(**remove_csrf(form.data))
        return redirect('/tipo_teste')

    rows = tipo_teste_dao.get_all()
    table = [row.to_mongo().to_dict() for row in rows]
    print(table, flush=True)
    return render_template('page.html', title='TipoTeste', table=table, forms=[form])
