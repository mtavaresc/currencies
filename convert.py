from requests import get


class Convert:
    def __init__(self):
        self.url = 'https://api.exchangerate-api.com/v4/latest/{currency}'

    def do(self, cur_orig, cur_dest, value):
        response = get(self.url.format(currency=cur_orig)).json()
        rates = response.get('rates')
        return round(rates.get(cur_dest) * value, 2)
