import random
from copy import deepcopy


class Matrix:
    def __init__(self, a, b=None):
        if b is not None:
            self.data = [[random.randint(-100, 100) for i in range(b)] for i in range(a)]
            self.shape = a, b
        else:
            self.data = deepcopy(a)
            self.shape = len(a), len(a[0])

    def check_shape_for_add(self, matrix):
        return self.shape == matrix.shape

    def check_shape_for_mul(self, matrix):
        return self.shape[1] == matrix.shape[0]

    def check_shape_square(self):
        return self.shape[0] == self.shape[1]

    def __add__(self, other):
        if self.check_shape_for_add(other):
            new = deepcopy(self.data)
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    new[x][y] += other.data[x][y]
            return Matrix(new)

    def __iadd__(self, other):
        if self.check_shape_for_add(other):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] += other.data[i][j]
            return self

    def __sub__(self, other):
        if self.check_shape_for_add(other):
            new = deepcopy(self.data)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new[i][j] -= other.data[i][j]
            return Matrix(new)

    def __isub__(self, other):
        if self.check_shape_for_add(other):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] -= other.data[i][j]
            return self

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            new = deepcopy(self.data)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new[i][j] *= other
            return Matrix(new)
        else:
            if self.check_shape_for_mul(other):
                new = [[0 for i in range(self.shape[0])] for y in range(other.shape[1])]
                for i in range(self.shape[0]):
                    for j in range(other.shape[1]):
                        for k in range(other.shape[0]):
                            new[i][j] += self.data[i][k] * other.data[k][j]
                return Matrix(new)

    def __imul__(self, other):
        self.data = self.__mul__(other)
        return self. data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Matrix:" \
               f"shape={self.shape}" \
               f"data={self.data}"

    def __setitem__(self, key1, key2, value):
        self.data[key1][key2] = value

    def __getitem__(self, item):
        return deepcopy(self.data[item])

    @staticmethod
    def __det(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            res = 0
            for i in range(len(matrix)):
                sub_data = []
                for row in range(1, len(matrix)):
                    sub_row = []
                    for col in range(len(matrix)):
                        if col == i:
                            continue
                        sub_row.append(matrix[row][col])
                    sub_data.append(sub_row)
                sub_matrix = Matrix(sub_data)
                if i % 2 == 0:
                    res += matrix[0][i] * sub_matrix.determinant()
                else:
                    res -= matrix[0][i] * sub_matrix.determinant()
            return res

    def determinant(self):
        if self.check_shape_square():
            matrix = self.data.copy()
            return self.__det(matrix)

    def is_degenerate(self):
        return self.determinant() == 0

    def gauss_solution(self, b):
        if not self.is_degenerate():
            matrix = deepcopy(self.data)
            rows, cols = self.shape
            b = b.copy()
            for col in range(cols):
                for row in range(col + 1, rows):
                    new_row = [-val * (matrix[row][col]) / matrix[col][col] for val in matrix[col]]
                    b[row] = b[row] - b[col] * matrix[row][col] / matrix[col][col]
                    matrix[row] = [sum(x) for x in zip(matrix[row], new_row)]
            x = []
            for row in reversed(range(rows)):
                x_row = b[row]
                i = 1
                for col in range(rows - row - 1):
                    x_row -= x[col] * matrix[row][0 - i]
                    i += 1
                x_row /= matrix[row][row]
                x.append(x_row)
            return x[::-1]

    def kramer_solution(self, b):
        if self.check_shape_square():
            x = []
            matrix = Matrix(self.data)
            det = matrix.determinant()
            for i in range(self.shape[0]):
                matrix.data = [list(x) for x in list(zip(*matrix.data))]
                matrix.data[i] = b
                matrix.data = [list(x) for x in list(zip(*matrix.data))]
                x.append(matrix.determinant() / det)
                matrix.data = self.data
            return x

    def inverse(self):
        if not self.is_degenerate() and self.check_shape_square():
            in_m = []
            edin_m = [[0 for i in range(self.shape[0])] for y in range(self.shape[1])]
            for i in range(self.shape[0]):
                edin_m[i][i] = 1
            for col in range(self.shape[0]):
                in_m.append(self.gauss_solution(edin_m[col]))
            in_m = [list(x) for x in zip(*in_m)]
            return Matrix(in_m)
