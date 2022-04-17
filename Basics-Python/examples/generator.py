jack = {
    'name': 'jack',
    'car': 'bmv'
}
john = {
    'name': 'john',
    'car': 'audi'

}
users = [jack, john]  # это список словарей
# создаем генератор по упрощенной схеме
cars = [person['car'] for person in users] #вводим переменную person для обращения к словарям в цикле, но будет ошибка,
# если ключа 'car' в словаре нет. Поэтому, будет правильным проверить наличие этого ключа и использовать метода get,
# также обратиться вторым аргументом в запрсове к словарю - аргумент по умолчанию ''
new_cars = [person.get('car', '') for person in users]

# создаем генератор по классической схеме
#cars = []
#for person in users:
#    cars.append(person['car'])
#    print(type(person)) # для контроля напролнения переменной person
#
print(cars)
print(new_cars)

"""
Т.е. сама модель генератора выглядит следующим образом:
(values) = [(expression) for (value) in (collection)]
или:
(values) = []
for (value) in (collection):
    (values).append( (expression) )

"""