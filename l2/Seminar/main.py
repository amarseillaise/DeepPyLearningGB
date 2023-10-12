import decimal
import math
from decimal import Decimal


def task4():
    # ✔Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
    # ✔Диаметр не превышает 1000 у.е. ✔Точность вычислений должна составлять не менее 42 знаков после запятой.
    # S = d2: l4 × π
    # Ь = π * d

    decimal.getcontext().prec = 42

    d = int(input("Введите диаметр: "))
    s = Decimal(d) * 2 / 4 * Decimal(math.pi)
    b = Decimal(math.pi) * Decimal(d)
    print(f"Площадь: {s}")
    print(f"Длина: {b}")


if __name__ == "__main__":
    task4()


