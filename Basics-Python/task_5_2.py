"""
Задание 5.2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

def odd_num_no_yield(to):
    return (x for x in range(1, to + 1, 2))


if __name__ == "__main__":
    b_gen = odd_num_no_yield(15)
    print("b_gen type", type(b_gen))
    for elem in b_gen:
        print(elem)

    print(f"empty {list(b_gen)}")