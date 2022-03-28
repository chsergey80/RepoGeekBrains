"""def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0
print(my_filter(numbers, is_even))

def is_not_even(number):
    return number % 2 != 0
print(my_filter(numbers, is_not_even))
"""

numbers = [5, 3, 4, 7, 8]
print(list(map(lambda x: x**2, numbers)))

print(list(map(lambda x: str(x), numbers)))
