from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

from convert import Convert
from model import Home

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Home(request.form)
    response = 0
    if request.method == 'POST' and form.validate_on_submit():
        response = Convert().do(form.currency_source.data, form.currency_destination.data, form.value_source.data)

    return render_template('home.html', form=form, response=response)
