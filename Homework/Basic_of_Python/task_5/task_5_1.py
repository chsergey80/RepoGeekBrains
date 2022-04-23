"""
Задание 5.1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
#1
#>>> next(odd_to_15)
#3
#...
#>>> next(odd_to_15)
#15
#>>> next(odd_to_15)
#...StopIteration...
"""


def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i


if __name__ == "__main__":
    a_gen = odd_num(15)
    print("a_gen type", type(a_gen))
    for elem in a_gen:
        print(elem)

    print(f"empty {list(a_gen)}")
