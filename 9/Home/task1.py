# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
from random import randint


def finding_root(*, a: int | float, b: int | float, c: int | float) -> tuple[int | float | None, int | float | None]:
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2


def rnd_csv():
    file_name = "random_file.csv"
    with open(file_name, "w", encoding="UTF-8") as f:
        csv_writer = csv.writer(f, delimiter=";", lineterminator="\n")
        csv_writer.writerow(["num1", "num2", "num3", ])
        csv_writer.writerows([[randint(-1000, 1000) for _ in range(3)] for _ in range(randint(100, 1000))])


# print(finding_root(a=4, b=-15, c=11))
rnd_csv()
