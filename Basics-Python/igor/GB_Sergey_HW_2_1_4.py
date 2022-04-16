# Это домашнее задание от Сергея от 28 марта Это ДЗ 2
# There is the homework _ 2
# Создать список кубов нечетных чисел от 1 до 1000
list_1 = []
for number in range (1, 1001):
    if number % 2 != 0:
        list_1.append(number**3)
print(list_1)
print(len(list_1))
# Создаем лист из Элементов (КУБЫ) сумму цифр каждого элемента должна делиться на 7 без остатка
# Эта функция считает сумму цифр в числе. Число передается через аргумент функции
def sum_digit(number):
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
def summ_multiple_seven(handle_list):
    free_list = []
    for item in handle_list:
        if sum_digit(item) % 7 == 0:
            free_list.append(item)
    print(free_list)
    print(len(free_list))
    # Последний шаг - считаем сумму элементов списка list_2
    summ_free_list = 0
    for item in free_list:
        summ_free_list += item
    return summ_free_list
print(summ_multiple_seven(list_1))
# Теперь к кубам прибавим 17 (list_17) и все снова посчитаем через функцию summ_multiple_seven(list_17)
list_17 = []
for item in list_1:
    item += 17
    list_17.append(item)
print(list_17)
print(summ_multiple_seven(list_17))
