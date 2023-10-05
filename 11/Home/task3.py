# Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle,
# который будет представлять прямоугольник с заданными шириной и высотой.
#
# Класс Rectangle должен иметь следующие атрибуты и методы:
#
# Атрибуты:
#
# width (int): ширина прямоугольника.
# height (int): высота прямоугольника.
#
# Методы:
#
# perimeter(): метод для вычисления периметра прямоугольника. Возвращает периметр как целое число.

# area(): метод для вычисления площади прямоугольника. Возвращает площадь как целое число.

# __add__(other): метод, позволяющий складывать два прямоугольника. Возвращает новый прямоугольник с шириной и высотой,
# равными сумме соответствующих атрибутов исходных прямоугольников.

# __sub__(other): метод, позволяющий вычитать один прямоугольник из другого.Возвращает новый
# прямоугольник с шириной и высотой, равными разности соответствующих атрибутов исходных прямоугольников.

# __lt__(other): метод, определяющий, является ли текущий прямоугольник меньше по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше площади другого, и False в противном случае.

# __eq__(other): метод, определяющий, равны ли два прямоугольника по площади. Возвращает True, если площади равны,
# и False в противном случае.

# __le__(other): метод, определяющий, меньше или равен текущий прямоугольник по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше или равна площади другого, и False в противном случае.

# __str__(): метод для получения строкового представления прямоугольника.
# Возвращает строку с информацией о ширине и высоте прямоугольника.

# __repr__(): метод для получения строкового представления прямоугольника,
# которое может быть использовано для создания нового объекта.


class Rectangle:

    def __init__(self, width: int, height: int):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError

    def perimeter(self):
        return (self.__height + self.__width) * 2

    def area(self):
        return self.__height * self.__width

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.__width + other.__width, float(self.__height + other.__height))

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.__width + other.__width > 0 and self.__height + other.__height > 0:
                return Rectangle(self.__width - other.__width, float(self.__height - other.__height))

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__width} и {self.__height}"

    def __repr__(self):
        return f"{self.__class__.__name__}{(self.__width, self.__height)}"
