"""
Задание 4.3* (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая
передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип
данных лучше использовать в ответе функции?
"""

import requests
import decimal


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        cur = respond.text.split(currency_code)
        if len(cur) == 1:
            return None
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        decimal.getcontext().prec = 2
        value = decimal.Decimal(value.replace(",", "."))
        date = respond.headers["Date"][5:-13]
        return (value, date)

    else:
        return None


print((currency_rates("Usd")))
print((currency_rates("eur")))
