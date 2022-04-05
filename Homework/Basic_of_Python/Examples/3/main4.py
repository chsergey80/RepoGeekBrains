def my_f(m):
    m = m[:]
    m.append(1)
    return m


a = [3]
print(my_f(a))
print(a)
