"""
Задача 3.2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"

"""


def num_translate_adv(num):
    nums = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    in_russian = None
    if num.lower() in nums:
        in_russian = nums[num.lower()]
        if num[0].isupper():
            in_russian = in_russian.title()

    return in_russian


print(num_translate_adv(input('Введите текстом числительное на Английском от 1 до 10: ')))
