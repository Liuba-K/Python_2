class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        d = [self.matrix[i] for i in range(len(self.matrix))]
        for x in d:
            x = str(x).strip("[]").replace(",", "  ")
            print(x)


    def __add__(self, other):
        if len(self.matrix[0]) == len(other.matrix[0]) and \
                len(self.matrix) == len(other.matrix):
            matrix_sum = [[self.matrix[i][j] + other.matrix[i][j]
                       for j in range(len(self.matrix[0]))]
                      for i in range(len(self.matrix))]
            return Matrix(matrix_sum)
        else:
            print("Матрицы разной длины")

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
matrix_3 = Matrix([[7, 8, 9], [9, 10, 11], [11, 12, 13]])
#print(matrix_1)
print(matrix_1 + matrix_2 + matrix_2)
