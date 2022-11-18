from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class TipoTesteForm(FlaskForm):
    id_tit = IntegerField("Id Tipo do Teste", validators=[DataRequired()])
    n_anac = IntegerField("Nº Anac", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired()])
    pontuacao_maxima = IntegerField("Pontuação Maxima", validators=[DataRequired()])
