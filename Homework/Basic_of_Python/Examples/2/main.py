import sys

nums_1 = [159, 45, 89] # список изменяемый
nums_2 = (159, 45, 89, [159, 57])  # кортеж неизменяемый - меньше места
nums_2[-1].append(56)
print(nums_2)
# print(sys.getsizeof(nums_2))  # 28 * 3 + 64
# print(sys.getsizeof(nums_2[0]))
# print(sys.getsizeof(nums_2[1]))
# print(sys.getsizeof(nums_2[2]))
# print(dir(nums_2))  # тьюпл, тапл
#nums_2[0] = 67
# print(sys.getsizeof(nums_1))  # 28 * 3 + 120
# print(sys.getsizeof(nums_1[0]))
# print(sys.getsizeof(nums_1[1]))
# print(sys.getsizeof(nums_1[2]))
# print(dir(nums_1))
# print(type(nums_1), id(nums_1))  #Ctrl /
# nums_2 = [159, 45, 89]
# print(type(nums_2), id(nums_2))
# nums_3 = nums_2.copy()
# print(type(nums_3), id(nums_3))
# nums_3.append("Hello")
# print(nums_2)