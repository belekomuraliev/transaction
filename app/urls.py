

from .views import app, index, transaction_create

app.add_url_rule('/', view_func=index, methods=['GET','POST'], endpoint='transaction')
app.add_url_rule('/create', view_func=transaction_create, methods=['GET','POST'], endpoint='create')
