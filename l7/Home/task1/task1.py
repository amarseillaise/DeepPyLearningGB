# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil
import string
from pathlib import Path
from random import randint

EXTENSIONS = {
    0: ["Audio", "mp3", "aac", "flac"],
    1: ["Video", "mp4", "avi", "mkv", "vbo"],
    2: ["Text", "txt", "ini"],
    3: ["Documents", "xlsx", "docx", "pdf"],
    # random unknown extension
    4: [''.join([string.ascii_lowercase[randint(0, 25)] if j != 0 else "Unknown"
                for i in range(randint(1, 5 if j != 0 else 1))]) for j in range(10)]
}


def generate_files(count):
    for i in range(count):
        extension = randint(0, len(EXTENSIONS.keys()) - 1)
        name = ''.join([string.ascii_lowercase[(randint(0, 25))] for _ in range(6)])
        with open(name + '.' + EXTENSIONS.get(extension)[randint(1, len(EXTENSIONS.get(extension)) - 1)], "w") as f:
            f.close()


def sort_files():
    for file in os.listdir():
        if file == __file__.split('.')[-1]:
            continue
        extension = file.split(".")[-1]
        for i in range(len(EXTENSIONS.keys()) - 1):
            group = EXTENSIONS.get(i)
            if extension in group:
                Path(group[0]).mkdir(exist_ok=True, parents=True)
                shutil.move(file, group[0])


generate_files(15)
sort_files()

