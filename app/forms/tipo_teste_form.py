from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField
from wtforms.validators import DataRequired


class TipoTesteForm(FlaskForm):
    id_tit = IntegerField("Id Tipo do Teste", validators=[DataRequired()])
    n_anac = IntegerField("Nº Anac", validators=[DataRequired()])
    nome = TextField("Nome", validators=[DataRequired()])
    pontuacao_maxima = IntegerField("Pontuação Maxima", validators=[DataRequired()])
