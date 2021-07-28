from flask import Blueprint, redirect, render_template

from app.dao import tecnico_dao
from app.forms import TecnicoForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('tecnico', __name__, static_folder="static", template_folder="templates")


@blue.route('/tecnico', methods=['GET', 'POST'])
def controlador():
    form = TecnicoForm()
    if form.validate_on_submit():
        tecnico_dao.insert(**remove_csrf(form.data))
        return redirect('/tecnico')

    rows = tecnico_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Técnico', table=table, forms=[form])
