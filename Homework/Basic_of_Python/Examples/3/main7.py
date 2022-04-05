user_1 = {'Фамилия': {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}, 'Имя': 'Иван',
          'Отчество': 'Иванович', 'Возраст': 23, 'Рост': 172, 'Вес': 65,
          'Город': 'Москва'}
print(f'Добрый день, {user_1["Фамилия"][1]}!')
user_1['Телефон'] = '+7(965)999-99-99'
print(user_1)
for key in user_1.keys():
    print(key)
for value in user_1.values():
    print(value)
for key, value in user_1.items():
    print(key, value)
user_1.pop('Телефон')
print(user_1)
print('Адрес' in user_1)
print(user_1.get('Адрес'))
