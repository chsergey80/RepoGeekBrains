def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var

    return int_func


f_n = ext_func()
print(f_n)
