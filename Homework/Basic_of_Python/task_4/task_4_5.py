"""
Задание 4.5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
Например: > python task_4_5.py USD
75.18, 2020-09-05
"""

import sys

import utils

code = 'GBP'
args = sys.argv
for code in args:
    conv = utils.currency_rates(code)
    if conv:
        cur, date = conv
        print(f"{cur}, {date}")
