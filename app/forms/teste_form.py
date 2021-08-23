from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

from app.dao import aviao_dao, tecnico_dao, tipo_teste_dao


class TesteForm(FlaskForm):
    aviao = SelectField("Avião", validators=[DataRequired()], choices=[(o.id, o.n_registro) for o in aviao_dao.get_all()])
    tecnico = SelectField("Técnico", validators=[DataRequired()], choices=[(o.id, o.n_membro) for o in tecnico_dao.get_all()])
    tipo_teste = SelectField("Tipo do Teste", validators=[DataRequired()], choices=[(o.id, o.n_anac) for o in tipo_teste_dao.get_all()])
    data_teste = DateField("Data", validators=[DataRequired()])
    horas_gastas = IntegerField("Horas Gastas", validators=[DataRequired()])
    pontuacao = IntegerField("Pontuação", validators=[DataRequired()])
