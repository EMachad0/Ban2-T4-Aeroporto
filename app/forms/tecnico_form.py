from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, DecimalField, FieldList, FormField
from wtforms.validators import DataRequired

from app.forms.modelo_form import ModeloForm


class TecnicoForm(FlaskForm):
    n_matricula = IntegerField("Nº Matricula", validators=[DataRequired()])
    n_membro = IntegerField("Nº Membro", validators=[DataRequired()])
    endereco = TextField("Endereço", validators=[])
    telefone = IntegerField("Telefone", validators=[])
    salario = DecimalField("Salario", validators=[DataRequired()])
    pericias = FieldList(FormField(ModeloForm), min_entries=2)
