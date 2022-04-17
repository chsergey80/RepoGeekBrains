# Это домашнее задание от Сергея от 28 марта Это ДЗ 2
# There is the homework _ 2
# Создать список кубов нечетных чисел от 1 до 1000
# Это вариант 2 сделаем его через генератолр списков
list_odd_numbers = [number**3 for number in range(1, 1001) if number % 2 != 0]
print(list_odd_numbers)
# Эта функция считает сумму цифр в числе. Число передается через аргумент функции
def sum_digit(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
# Опять генератором делаем список сумм
list_summs_numbers = [sum_digit(item) for item in list_odd_numbers]
print(list_summs_numbers)
# Теперь делаем список из элементов list_2 кратных 7
list_mutuple_seven = [item for item in list_summs_numbers if item % 7 == 0]
print(list_mutuple_seven)
# Последний шаг - считаем сумму элементов списка list_3
summ_list_3 = 0
for item in list_mutuple_seven:
    summ_list_3 += item
print(summ_list_3)


