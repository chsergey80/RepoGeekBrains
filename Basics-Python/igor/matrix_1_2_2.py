
lst_1 = [[1, 4, 6, 2], [1, 1, 1, 4], [2, 5, 6, 1]]
lst_2 = [[1, 3, 3, 3], [2, 2, 5, 5], [3, 4, 7, 3]]

class Matrix:

    def __init__(self, mat_1, mat_2):
        self.mat_1 = mat_1
        self.mat_2 = mat_2

    def __add__(self):
        self.matr = [[self.mat_1[i][j] + self.mat_2[i][j] for j in range(len(self.mat_1[0]))] for i in range(len(self.mat_1))]
        self.str_matr = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))
        return str(f'Матрица 3 итоговая\n{self.str_matr}')

    def __str__(self):
        self.str_1 = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.mat_1]))
        self.str_2 = str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.mat_2]))
        return (f'Матрица 1\n{self.str_1}\nМатрица 2\n{self.str_2}')


my_matrix = Matrix(lst_1, lst_2)
print(my_matrix)
print(my_matrix.__add__())
