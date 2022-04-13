# Это домашнее задание от Сергея от 28 марта Это ДЗ 2
# There is the homework _ 2
# Создать список кубов нечетных чисел от 1 до 1000
list_1 = []
for number in range (1, 1001):
    if number % 2 != 0:
        list_1.append(number**3)
print(list_1)
print(len(list_1))
# Создаем лист из сумму цифр каждого элемента листа с кубами (list_1)
list_2 = []
# Эта функция считает сумму цифр в числе. Число передается через аргумент функции
def sum_digit(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
for item in list_1:
    list_2.append(sum_digit(item))
print(list_2)
print(len(list_2))
# Теперь делаем список из элементов list_2 кратных 7
list_3 = []
for item in list_2:
    if item % 7 == 0:
        list_3.append(item)
print(list_3)
# Последний шаг - считаем сумму элементов списка list_3
summ_list_3 = 0
for item in list_3:
    summ_list_3 += item
print(summ_list_3)
