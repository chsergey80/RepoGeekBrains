"""
Задание 3.3: Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
Примечание. Списки создайте вручную, например так:

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
В этом случае ответ будет: [5, 8]
"""

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in my_list_1:
    if my_list_1.count(number) == 1:  # Сколько раз число входит в список
        result.append(number)
print(result)