class MyOwnErr(Exception):
    pass


in_data = input("Enter a positive number")
try:
    in_data = int(in_data)
    if in_data < 0:
        raise MyOwnErr("Only positive!")
except ValueError as err:
    print(err)
except MyOwnErr:
    in_data = -in_data
    print(f"Corrected data: {in_data}")
else:
    print(in_data)