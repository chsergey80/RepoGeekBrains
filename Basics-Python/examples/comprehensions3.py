# Еще пример. Решим задачу посложнее. Нам необходимо сделать данные плоскими (flat). Например, мы записывали
# данные о температуре воздуха в отдельную строку таблицы (списка) каждый день. Теперь нам нужен непрерывный ряд данных
# о температуре: не по дням, а в виде одномерного списка. Зачем?
# Например, чтобы построить график изменения температуры в течение недели (месяца, полугодия и т.д.)
# То есть от двумерных данных нужно перейти к одномерным (плоским). Решаем задачу через цикл:

weather_data = [
    [-17.5, -18.9, -21.0, -16.1],
    [-9.3, -11.7, -14.3, -15.8],
]
flat_weather_data = []
for row in weather_data:
    for el in row:
        flat_weather_data.append(el)
print(flat_weather_data)

# Теперь решим задачу через List Comprehensions:
flat_weather_data1 = [el for row in weather_data for el in row]
print(flat_weather_data1)

# Решение в одну строку. Надо только научиться «читать» такой код. Можно переформатировать:
flat_weather_data2 = [
    el for row in weather_data
        for el in row
]
print(flat_weather_data2)

# А если нам нужно ещё отфильтровать данные? Например, берём только температуры до –20 градусов:
flat_weather_data_3 = [
    el for row in weather_data for el in row
    if el > -20
]
print(flat_weather_data_3)