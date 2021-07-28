from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField
from wtforms.validators import DataRequired


class TesteForm(FlaskForm):
    id_tes = IntegerField("Id Teste", validators=[DataRequired()])
    id_avi = IntegerField("Id Avião", validators=[DataRequired()])
    id_fun = IntegerField("Id Técnico", validators=[DataRequired()])
    id_tit = IntegerField("Id Tipo do Teste", validators=[DataRequired()])
    data_teste = DateField("Data", validators=[DataRequired()])
    horas_gastas = IntegerField("Horas Gastas", validators=[DataRequired()])
    pontuacao = IntegerField("Pontuação", validators=[DataRequired()])
