basket = [159.78, 67, 67.87]
print(basket)
new_items = [46.78, 34.89]
for el in new_items:
    basket.append(el)
print(basket)
basket.extend(new_items)
print(basket)
basket.append(new_items)
print(basket)
basket += new_items
print(basket)
last_item = basket.pop()  # O(1)
print(basket)
print(last_item)
some_item = basket.pop(1)  # O(n)
print(some_item)
print(basket)
basket.insert(2, 155)  # O(n)
print(basket)
basket.remove(46.78)
print(basket)
item = 34.89
while item in basket:
    basket.remove(item)
print(basket)
basket.reverse()  # на месте
print(basket)
basket_r = list(reversed(basket))
print(basket_r)
#print(*basket_r)
# for el in basket_r:
#     print(el)
# срезы(слайсы)
print(basket[:3]) # start = 0 : stop не включительно = len : step = 1
print(basket[:])  # копия и глубокая deepcopy
print(basket[:1000])
print(basket[1:6:2])
print("revolution"[::-1])
basket.pop(1)
basket *= 4
print(basket)
basket.sort()  # на месте
print(basket)
basket_s = sorted(basket, reverse=True)  # не на месте
print(basket_s)
ind = basket_s.index(159.78, 1)  # первое вхождение
print(ind)
print(basket.count(159.78))  # сколько раз встречается
