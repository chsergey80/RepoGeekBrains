import re

text = 'сегодня 21 апреля 2022 года. Идёт 8 урок по Python'

pattern = re.compile(r'год')
help(re.compile)
result = re.search(pattern, text)  # первое вхождение Match
result = pattern.search(text)   # работает быстрее, превращаем функцию в метод.
help(pattern.search)
print(result.span())
print(dir(result))
print(result)

all_result = re.findall(pattern, text)
all_result = pattern.findall(text)
print(all_result)  # все вхождения в виде списка строк

result_iter = re.finditer(pattern, text)  # все вхождения в виде Match
result_iter = pattern.finditer(text)
print(*result_iter)

result_match = re.match(pattern, text)  # ищет только в начале текста
result_match = pattern.match(text)
print(result_match)

