#Задание 2.3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
# имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
# (Формула не соответствует реальной действительности и здесь используется только ради примера)

# Решение задания 2.3

name = str(input('Введите имя и фамилию '))
age = int(input('Сколько вам лет? '))
weight = int(input('Сколько вы весите? '))

if age <= 30 and weight >= 50 and weight <= 120:
    print(name, age, 'год, вес', weight, ' - хорошее состояние')
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(name, age, 'год, вес', weight, ' - следует заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, age, 'год, вес', weight, ' - следует обратится к врачу')
else:
    print(name, age, 'год, вес', weight, ' - жить будете')