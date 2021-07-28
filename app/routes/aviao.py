from flask import Blueprint, redirect, render_template

from app.dao import aviao_dao, modelo_dao
from app.forms import AviaoForm, ModeloForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('aviao', __name__, static_folder="static", template_folder="templates")


@blue.route('/aviao', methods=['GET', 'POST'])
def aviao():
    aviao_form = AviaoForm()
    if aviao_form.validate_on_submit():
        aviao_dao.insert(**remove_csrf(aviao_form.data))
        return redirect('/aviao')

    modelo_form = ModeloForm()
    if modelo_form.validate_on_submit():
        modelo_dao.insert(**remove_csrf(modelo_form.data))
        return redirect('/aviao')

    rows = aviao_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Avião', table=table, forms=[aviao_form, modelo_form])
