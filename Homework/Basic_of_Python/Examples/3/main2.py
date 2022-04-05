def my_sum(x, y):
    return x + y, False, 6


my_sum2 = lambda x, y: x + y
print(my_sum2(6, 8))
print((lambda x, y: x + y)(5, 4))

a = ['first3', 'second2', 'third1']
a.sort(key=lambda x: x[-1])
print(a)

# print(my_sum(1, 5))
# f = my_sum(1, 5)[0] + my_sum(5, 8)[0] * 2 + 5
# print(f)
