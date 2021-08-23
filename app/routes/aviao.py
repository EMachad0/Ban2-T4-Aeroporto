from flask import Blueprint, redirect, render_template
from flask_mongoengine.wtf import model_form

from app.models import Aviao
from app.dao import aviao_dao, modelo_dao
from app.forms import AviaoForm, ModeloForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('aviao', __name__, static_folder="static", template_folder="templates")


@blue.route('/aviao', methods=['GET', 'POST'])
def aviao():
    aviao_form = AviaoForm()
    if aviao_form.validate_on_submit():
        print(remove_csrf(aviao_form.data), flush=True)
        aviao_dao.insert(**remove_csrf(aviao_form.data))
        return redirect('/aviao')

    rows = aviao_dao.get_all()
    table = [row.to_mongo().to_dict() for row in rows]
    return render_template('page.html', title='Avião', table=table, forms=[aviao_form])
