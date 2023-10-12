# Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:
#
# Инициализация матрицы. Конструктор класса должен принимать количество строк rows
# и количество столбцов cols и создавать матрицу с нулевыми значениями.
#
# Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.
#
# Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными размерами
# (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).
#
# Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.
#
# Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы,
# где элементы строки разделены пробелами, а строки сами разделены символами новой строки.
#
# Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__,
# который возвращает строку, которую можно использовать для создания нового объекта класса Matrix.

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [] if rows == 0 and cols == 0 else [[2 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        lst = []
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                temp_lst = []
                for j in range(self.cols):
                    temp = self.data[i][j] + other.data[i][j]
                    temp_lst.append(temp)
                lst.append(temp_lst)
            new_instance = Matrix(0, 0)
            new_instance.data = lst
            new_instance.rows = self.rows
            new_instance.cols = self.cols
            return new_instance

    def __str__(self):
        lst = ""
        for i in range(self.rows):
            for j in range(self.cols):
                lst += str(self.data[i][j]) + " "
            lst += "\n"
        return lst.replace(" \n", "\n")[0:-1]

    def __mul__(self, other):
        lst = []
        if isinstance(other, Matrix) and self.cols == other.rows:
            for i in range(self.rows):
                temp_lst = []
                for j in range(other.cols):
                    temp = 0
                    for k in range(self.cols):
                        temp += self.data[i][k] * other.data[k][j]
                    temp_lst.append(temp)
                lst.append(temp_lst)
            new_instance = Matrix(0, 0)
            new_instance.data = lst
            new_instance.rows = self.rows
            new_instance.cols = other.cols
            return new_instance

    def __eq__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        return False
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}{(self.rows, self.cols)}"


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
