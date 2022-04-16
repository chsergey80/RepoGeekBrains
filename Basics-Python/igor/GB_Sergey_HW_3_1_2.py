# Это домашнее задание от Сергея от 28 марта Это ДЗ 3
# There is the homework _ 3
# Нужно просклонять число от 1 до 100 как проценты
#  Типа 1 процент , два процента , пять процентов и вывести это в столбик

list_numbers = [item for item in range(1, 101)] # генератором делаю список от 1 до 100

def select_digit_word_1(handle_list):# В этой функции выбираю числа подходящие под слво "процент"
    dictionary_1 = {}                # и заношу их в словарь
    for item in handle_list:
        if item % 10 == 1 and item != 11:
            key = item
            vol = 'процент'
            dictionary_1[key] = vol
    return dictionary_1

def select_digit_word_2(handle_list):# В этой функции выбираю числа подходящие под слво "процента"
    dictionary_2 ={}                 # и заношу их в словарь
    for item in handle_list:
       if 1 < item % 10 < 5:
        key = item
        vol = 'процента'
        dictionary_2[key] = vol
        if 11 < item < 15:
            del dictionary_2[item]
    return dictionary_2

def select_digit_word_3(handle_list):# В этой функции выбираю числа подходящие под слво "процентов"
    dictionary_3 = {}                # и заношу их в словарь
    for item in handle_list:
        if 4 < item % 10 < 10 or 4 < item < 15 or item % 10 == 0:
            key = item
            vol = 'процентов'
            dictionary_3[key] = vol
    return dictionary_3

result_1 = select_digit_word_1(list_numbers)
result_2 = select_digit_word_2(list_numbers)
result_3 = select_digit_word_3(list_numbers)

dictionary = result_1|result_2|result_3 # Объединяю словари
list_key_dict = list(dictionary.keys()) # эта строка и строка ниже - упорядочиваю ключи
list_key_dict.sort()
for i in list_key_dict:                 # эти две строки вывод на печать
    print(i,'', dictionary[i])



