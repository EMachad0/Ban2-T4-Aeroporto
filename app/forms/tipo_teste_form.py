from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField
from wtforms.validators import DataRequired


class TipoTesteForm(FlaskForm):
    n_anac = IntegerField("Nº ANAC", validators=[DataRequired()])
    nome = TextField("Nome", validators=[DataRequired()])
    pontuacao_maxima = IntegerField("Pontuação Maxima", validators=[DataRequired()])
