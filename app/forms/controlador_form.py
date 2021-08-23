from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ControladorForm(FlaskForm):
    data_exame = DateField("Data Exame", validators=[DataRequired()])
    n_matricula = IntegerField("Nº Matricula", validators=[DataRequired()])
    n_membro = IntegerField("Nº Membro", validators=[DataRequired()])
