def my_f(value, a=[]):
    a.append(value)
    return a


print(my_f(6, [4, 5]))
print(my_f(6))
print(my_f(7))
