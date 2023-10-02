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
from typing import Callable


def calculate_root_from_csv(func_csv: Callable):
    def deco(func_root):
        def wrapper():
            with open(func_csv(), "r", encoding="UTF-8") as f:
                csv_reader = csv.reader(f, delimiter=";")
                for row in csv_reader:
                    root = func_root()!!!!!!!!!!!!!!!!!!!!!
                    print(f"{row} -> {func_root}")

        return wrapper
    return deco


def gen_csv():
    file_name = "random_file.csv"
    with open(file_name, "w", encoding="UTF-8") as f:
        csv_writer = csv.writer(f, delimiter=";", lineterminator="\n")
        csv_writer.writerows([[randint(-1000, 1000) for _ in range(3)] for _ in range(randint(100, 1000))])
    return file_name


@calculate_root_from_csv(gen_csv)
def finding_root(*, a: int | float, b: int | float, c: int | float) -> tuple[int | float | None, int | float | None]:
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2


finding_root()




# print(finding_root(a=4, b=-15, c=11))
# gen_csv()
