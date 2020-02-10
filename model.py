from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, SelectField, StringField, validators

CURRENCIES = [('BRL', 'Brazilian Real'),
              ('USD', 'American Dollar'),
              ('CAD', 'Canadian Dollar'),
              ('EUR', 'Euro'),
              ('AUD', 'Australian Dollar')]


class Home(FlaskForm):
    currency_source = SelectField('Currency From', choices=CURRENCIES)
    value_source = IntegerField('From', [validators.DataRequired()])
    currency_destination = SelectField('Currency Destination', choices=CURRENCIES)
    value_destination = StringField('To')
    submit = SubmitField('Submit')
