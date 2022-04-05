num = input('Enter a number: ')
try:
    num = int(num)
    print(num)
except (ValueError, TypeError) as err3:
    print('Error1!')
    print(err3)
except ZeroDivisionError:
    print('Error2!')