from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators

from .models import Transactions

class TransactionsForm(FlaskForm):

    value = IntegerField(label='Сумма транзакции', validators=[validators.DataRequired()])
    status = StringField(label='Статус карты', validators=[validators.DataRequired()])
    unit = StringField(label='Тип валюты', validators=[validators.DataRequired()])
    comment = StringField(label='Коментарии транзакции', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить')




