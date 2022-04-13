from random import randint
from time import perf_counter, time

nums = []
for _ in range(10 ** 6):
    nums.append(randint(1, 1000))

start = perf_counter()
nums_sum = 0
idx = 0
while idx < len(nums):
    nums_sum += nums[idx]
    idx += 1
print(nums_sum, perf_counter() - start)

start = perf_counter()
nums_sum2 = 0
for num in nums:
    nums_sum2 += num
print(nums_sum2, perf_counter() - start)

start = perf_counter()
nums_sum3 = sum(nums)
print(nums_sum3, perf_counter() - start)
