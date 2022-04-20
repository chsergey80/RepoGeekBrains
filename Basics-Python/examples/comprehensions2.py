# Еще пример List Comprehensions. Здесь речь пойдет о вложенном списке.
# Внутри List Comprehensions можно использовать List Comprehensions — получаем Nested List Comprehensions. Например,
# нам необходимо сложить две матрицы. Можем решить задачу наивным # способом:

matrix_1 = [
    [1, 4, 3, 3],
    [15, 0, 8, 11],
]
matrix_2 = [
    [17, 3, 2, 8],
    [4, 3, 6, 4],
]
matrix_sum = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[0])):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_sum.append(row)
print(*matrix_sum, sep='\n')

# Или
matrix_sum = [
[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))]
for i in range(len(matrix_1))
]

# Или через zip()
matrix_sum = [
[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
for row_1, row_2 in zip(matrix_1, matrix_2)
]