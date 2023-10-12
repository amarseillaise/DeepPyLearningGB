# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import csv
import json
from random import randint
from typing import Callable
from math import sqrt

CSV_FILE = "random_file.csv"
JSON_FILE = "random_file.json"


def calculate_root_from_csv(csv_generator: Callable):
    def deco(func_root: Callable):
        csv_generator()

        def wrapper(*args, **kwargs):
            result = {}
            with open(CSV_FILE, "r", encoding="UTF-l8") as f:
                csv_reader = csv.reader(f, delimiter=";")
                for row in csv_reader:
                    a, b, c = row
                    x1, x2 = func_root(int(a), int(b), int(c))
                    result[f"{x1 = } ; {x2 = }"] = row
            return result
        return wrapper
    return deco


def roots_to_json(func: Callable):
    def wrapper(*args, **kwargs):
        with open(JSON_FILE, "w", encoding="UTF-l8") as f:
            json.dump(func(), f, indent=4)
        return True
    return wrapper


def gen_csv():
    with open(CSV_FILE, "w", encoding="UTF-l8") as f:
        csv_writer = csv.writer(f, delimiter=";", lineterminator="\n")
        csv_writer.writerows([[randint(-1000, 1000) for _ in range(3)] for _ in range(randint(100, 1000))])


@roots_to_json
@calculate_root_from_csv(gen_csv)
def finding_root(a: int | float, b: int | float, c: int | float) -> tuple[int | float | None, int | float | None]:
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    return x1, x2


finding_root()
