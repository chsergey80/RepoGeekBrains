import re

text = 'сегодня 21 апреля 2022 года. АБВГ Идёт 8 урок по Python. Следующий 9 мая 2023 года.'

#pattern = re.compile(r'год')
pattern = re.compile(r'\d')  # любая цифра - селектор \ d - селектор: цифра
pattern = re.compile(r'\d+')  # одна или несколько цифр
pattern = re.compile(r'\d?')  # 0 или 1 цифр
pattern = re.compile(r'\d*')  # 0 или несколько цифр
                                # {} - указываются параметры квантификатора
pattern = re.compile(r'\d{2,3}') # указание на количество цифр: от 2 до 3 цифр
pattern = re.compile(r'\d{2,}') # указание на количество цифр: от 2 до бесконечности - цифр
pattern = re.compile(r'\d{,3}')  # указание на количество цифр: от 0 до 3 цифр
pattern = re.compile(r'\d{2}')  # указание на количество цифр: 2 цифр
pattern = re.compile(r'\w+')  # w - селектор:буква, цифра, _
pattern = re.compile(r'\s')  # s - селектор:пробелы, переводы строк, табуляторы
pattern = re.compile(r'.') # '.' - селектор:любой символ
pattern = re.compile(r'\.')  # '\.'- селектор:точка.  Экранируем точку с помощью бэк слэша.
pattern = re.compile(r'[Pyt]') # найти символы, указанные в []
pattern = re.compile(r'[^Pyt]')  # найти символы, кроме указанных в [].
pattern = re.compile(r'[Pyt.]')   # найти точку и буквы P y t.
pattern = re.compile(r'[а-пё]')    # найти символы русской кирилицы от а до п с ё
pattern = re.compile(r'[А-в]+')    # найти символы русской кирилицы от а до в и все заглавные, одна или несколько букв
pattern = re.compile(r'^[сегодня]')  # с начала текста
pattern = re.compile(r'[Python]$')  # с конца текста
pattern = re.compile(r'^[Pyt]$')   # с начала текста и с конца текста, т.е. текст должен полностью совпадать
pattern = re.compile(r'Python$')  # полное совпадение в тексет с конца
pattern = re.compile(r'Python|Идёт|урок')  # | - означает 'или'
                               # далее идут группы условий
pattern = re.compile(r'\b(\w+)\b')  # границы слова \b,  w+ - любая буква, цифра и _ в словах, которые выбираем
pattern = re.compile(r'\s')  # выбираем пробелы, \s - означает любой пробельный символ
pattern = re.compile(r'\d{1,2}\s(\w+)\s\d{4}')
pattern = re.compile(r'(?P<day>\d{1,2})\s(?P<month>\w+)\s(?P<year>\d{4})')

#all_result = pattern.findall(text)
#print(all_result)  # все вхождения в виде списка строк
#
result_iter = pattern.finditer(text)
for res in result_iter:
     print(res.groups())  # найденные группы
     print(res.group(0))  # всё, что на сработала регулярка
     print(res.group(1))  # первая группа, нумерация с 1
     print(res.group(2))
     print(res.group(3))
     print(res.groupdict())
