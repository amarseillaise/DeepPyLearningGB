# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌Имя файла должно совпадать с именем декорируемой функции.

import json
import os
from typing import Callable


def decor(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        filename = func.__name__ + '.json'
        if filename in os.listdir():
            with open(filename, 'r', encoding="UTF-8") as f:
                data = json.load(f)
        else:
            data = dict()

        result = func(*args, **kwargs)
        data[result] = tuple(args) + tuple(kwargs.items())

        with open(filename, 'w', encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    return wrapper


@decor
def funcjh(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())


funcjh(5, 17, 18, 24)
funcjh(82, 17, 18, 24, a=16, sdf=48)
