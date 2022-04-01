GREETING = 'Уважаемый {}, поздравляем Вас с праздником {}!'
party = '1 мая'
names = ['Иван', 'Сергей', 'Даниил']
for name in names:
    #print(GREETING.format(name, party))
    #print("Уважаемый %s, поздравляем Вас с праздником %s!" % (name, party))
    print(f"Уважаемый {name}, поздравляем Вас с праздником {party}!")

age = 5
print(f"возраст {age:05d}")
price = 678.454856223421346325
print(f"цена: {price:.5f}")
print(round(price, 8))
name = "Иван"
print(f"Уважаемый {name:>25}!")
print(f"Уважаемый {name:<25}!")
print(f"Уважаемый {name:^25}!")