from flask_wtf import FlaskForm
from wtforms import IntegerField, FormField
from wtforms.validators import DataRequired
from app.forms.modelo_form import ModeloForm


class AviaoForm(FlaskForm):
    n_registro = IntegerField("Nº Registro", validators=[DataRequired()])
    modelo = FormField(ModeloForm)
