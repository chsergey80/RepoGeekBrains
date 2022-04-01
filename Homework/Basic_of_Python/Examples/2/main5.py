num = input("Enter a number: ")
print(True if num.isdigit() else None)  # тернарный оператор
if num.isdigit():
    print(True)
else:
    print(None)
print(num.isdigit() or None)
print(num.isdigit())

# walrus - морж