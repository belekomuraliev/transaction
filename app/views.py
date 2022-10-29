from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Transactions
from .forms import TransactionsForm



def index():
    title = 'Список транзакции'
    transactions = Transactions.query.all()
    return render_template('index.html', transactions=transactions, title=title)


def transaction_create():
    title = 'Транзакция'
    form = TransactionsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            transaction = Transactions()
            form.populate_obj(transaction)
            db.session.add(transaction)
            db.session.commit()
            flash(f'Транзакция {transaction.value} успешно добавлено', 'success')
            return redirect(url_for('transaction'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
    return render_template('transaction_form.html', form=form, title=title)


