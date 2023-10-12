# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается
# при некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.

class NegativeValueError(Exception):
    pass


class Validator:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        getattr(instance, self.param_name)

    def __set__(self, instance, value):
        side = "Ширина" if self.param_name == "__Rectangle__width" else "Высота"
        if value < 0:
            raise NegativeValueError(f"{side} должна быть положительной, а не {value}")
        setattr(instance, self.param_name, value)


class Rectangle:
    __width = Validator()
    __height = Validator()

    def __init__(self, width: int, height: int = 5):
        self.__width = width
        self.__height = height

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


r = Rectangle(-1, 14)
