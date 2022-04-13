from sys import getsizeof
from time import perf_counter

MAX_NUM = 10 ** 7


def nums_gen():
    for num in range(1, MAX_NUM + 1):
        if num % 7 == 0:
            yield num


start = perf_counter()
nums = []
for num in range(1, MAX_NUM + 1):
    if num % 7 == 0:
        nums.append(num)
# print(nums)
print(getsizeof(nums))
print(sum(nums))
print(1, perf_counter() - start)

start = perf_counter()
result = 0
for num in range(1, MAX_NUM + 1):
    if num % 7 == 0:
        result += num
print(result)
print(2, perf_counter() - start)

start = perf_counter()
nums = nums_gen()
print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(*nums)
print(sum(nums))
print(getsizeof(nums))
print(3, perf_counter() - start)

start = perf_counter()
nums = (num for num in range(1, MAX_NUM + 1) if num % 7 == 0)
print(nums)
print(sum(nums))
print(getsizeof(nums))
print(4, perf_counter() - start)

nums = (num if num % 7 == 0 else num ** 2 for num in range(1, MAX_NUM + 1))
print(sum(nums))

start = perf_counter()
nums = [num for num in range(1, MAX_NUM + 1) if num % 7 == 0]
print(sum(nums))
print(5, perf_counter() - start)

nums = {num if num % 7 == 0 else num ** 2: num ** 2 for num in range(1, MAX_NUM + 1) if num % 7 == 0}

nums = {num for num in range(1, MAX_NUM + 1) if num % 7 == 0}
