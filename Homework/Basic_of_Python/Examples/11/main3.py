try:
    res = 100 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print(res)
finally:
    print("The end")

