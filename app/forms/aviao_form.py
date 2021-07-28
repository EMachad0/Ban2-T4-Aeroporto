from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class AviaoForm(FlaskForm):
    id_avi = IntegerField("Id Avião")
    id_mod = IntegerField("Id Modelo", validators=[DataRequired()])
    n_registro = IntegerField("Nº Registro", validators=[DataRequired()])
