import re

text = 'сегодня 21 апреля 2022 года. Идёт 8 урок по Python. Следующий 9 мая 2023 года'

#pattern = re.compile(r'год')
pattern = re.compile(r'\d')  # любая цифра - селектор
pattern = re.compile(r'\d+')  # одна или несколько
pattern = re.compile(r'\d?')  # 0 или 1
pattern = re.compile(r'\d*')  # 0 или несколько
pattern = re.compile(r'\d{2,3}')
pattern = re.compile(r'\d{2,}')
pattern = re.compile(r'\d{,3}')
pattern = re.compile(r'\d{2}')
pattern = re.compile(r'\w+')  # буква, цифра, _
pattern = re.compile(r'\s')  # пробелы, переводы строк, табуляторы
pattern = re.compile(r'.') # любой символ
pattern = re.compile(r'\.')  # точка
pattern = re.compile(r'[Pyt]')
pattern = re.compile(r'[^Pyt]')  # кроме
pattern = re.compile(r'[Pyt.]')
pattern = re.compile(r'[а-пё]')
pattern = re.compile(r'[А-в]+')
pattern = re.compile(r'^[сегодня]')  # с начала текста
pattern = re.compile(r'[Python]$')  # с конца текста
pattern = re.compile(r'^[Pyt]$')
pattern = re.compile(r'Python$')
pattern = re.compile(r'Python|Идёт|урок')
pattern = re.compile(r'\b(\w+)\b')  # границы слова \b
pattern = re.compile(r'(?P<day>\d{1,2})\s(?P<month>\w+)\s(?P<year>\d{4})')

# all_result = pattern.findall(text)
# print(all_result)  # все вхождения в виде списка строк

result_iter = pattern.finditer(text)
for res in result_iter:
    print(res.groups())  # найденные группы
    print(res.group(0))  # всё, что на сработала регулярка
    print(res.group(1))  # первая группа, нумерация с 1
    print(res.group(2))
    print(res.group(3))
    print(res.groupdict())
