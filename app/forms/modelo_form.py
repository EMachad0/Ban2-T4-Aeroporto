from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class ModeloForm(FlaskForm):
    cod = StringField("Cod Modelo", validators=[DataRequired()])
    capacidade = IntegerField("Capacidade", validators=[DataRequired()])
    peso = IntegerField("Peso", validators=[DataRequired()])
