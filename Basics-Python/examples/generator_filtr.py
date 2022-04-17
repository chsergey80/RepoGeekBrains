# Фильтрация
names = ['jack', 'john', 'oleg', 'ula']
# создаем генератор по упрощенной схеме
new_names = [n for n in names if n.startswith('j')] # фильтруем имена по первой букве
# создаем генератор по классической схеме
#new_names = []
#for n in names:
#    if n.startswith('j'):
#        new_names.append(n)

print(new_names)


"""
Т.е. сама модель генератора выглядит следующим образом:
(values) = [(expression) for (value) in (collection) if (condition)]
или:
(values) = []
for (value) in (collection):
    if (condition):
    (values).append( (expression) )

"""