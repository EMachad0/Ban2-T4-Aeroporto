from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, DecimalField
from wtforms.validators import DataRequired


class TecnicoForm(FlaskForm):
    id_fun = IntegerField("Id Funcionário", validators=[DataRequired()])
    endereco = TextField("Endereço", validators=[DataRequired()])
    telefone = IntegerField("Telefone", validators=[DataRequired()])
    salario = DecimalField("Salario", validators=[DataRequired()])
    n_matricula = IntegerField("Nº Matricula", validators=[DataRequired()])
    n_membro = IntegerField("Nº Membro", validators=[DataRequired()])
