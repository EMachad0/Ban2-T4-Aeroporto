from flask import Blueprint, redirect, render_template

from app.dao import controlador_dao
from app.forms import ControladorForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('controlador', __name__, static_folder="static", template_folder="templates")


@blue.route('/controlador', methods=['GET', 'POST'])
def controlador():
    form = ControladorForm()
    if form.validate_on_submit():
        controlador_dao.insert(**remove_csrf(form.data))
        return redirect('/controlador')

    rows = controlador_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Controlador', table=table, forms=[form])
