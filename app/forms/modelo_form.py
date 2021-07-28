from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class ModeloForm(FlaskForm):
    id_mod = IntegerField("Id Modelo")
    cod = IntegerField("Cod Modelo", validators=[DataRequired()])
    capacidade = IntegerField("Capacidade", validators=[DataRequired()])
    peso = IntegerField("Peso", validators=[DataRequired()])
