# to convert from one currency to another currency we can  use to lib  forex_python and tinker(but the tinker is used for creating web api )
from forex_python.converter import CurrencyRates
from datetime import datetime,time


def currency_conversion(from_curr,to_curr,val):
    ls = []
    date_obj = datetime.today()
    c = CurrencyRates()
    for to_val in to_curr:
        conn = c.convert(from_curr,to_val,val)
        ls.append(conn)
    print(ls)

if __name__ == '__main__':
    from_curr ='USD'
    to_curr = ['INR','EUR']
    val = 10
    currency_conversion(from_curr,to_curr,val)

