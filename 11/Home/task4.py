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
        self.__lst = [] if rows == 0 and cols == 0 else [[1 for _ in range(rows)] for _ in range(cols)]

    def __add__(self, other):
        lst = []
        if isinstance(other, Matrix):
            for i in range(self.rows):
                temp_lst = []
                for j in range(self.cols):
                    temp = self.__lst[i][j] + other.__lst[i][j]
                    temp_lst.append(temp)
                lst.append(temp_lst)
        new_instance = Matrix(0, 0)
        new_instance.__lst = lst
        new_instance.rows = self.rows
        new_instance.cols = self.cols
        return new_instance

    def __str__(self):
        lst = ""
        for i in range(self.rows):
            for j in range(self.cols):
                lst += str(self.__lst[i][j]) + " "
            lst += "\n"
        return lst.replace(" \n", "\n")


a = Matrix(3, 3)
b = Matrix(3, 3)
c = a + b
print(c)
