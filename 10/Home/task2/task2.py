# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
import csv
import json
import pickle
import os
import shutil
import string
from pathlib import Path
from random import randint


# 1
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


class DirTraverser:
    def __init__(self, path: str):
        self.__path = path
        self.data = []

    def change_path(self, new_path: str):
        self.__path = new_path

    def show_path(self):
        return self.__path

    def gen_list(self):
        result = []
        for root, dirs, files in os.walk(self.__path):
            dir_size = 0
            for file in files:
                file_path = os.path.join(root, file)

                size = os.path.getsize(file_path)
                dir_size += size

                file_info = {
                    'name': file,
                    'type': 'file',
                    'size': size,
                    'parent_directory': root
                }
                result.append(file_info)

            dir_info = {
                'name': os.path.basename(root),
                'type': 'directory',
                'size': dir_size,
                'parent_directory': os.path.dirname(root)
            }
            result.append(dir_info)
        self.data = result

    def write_to_json(self, json_name: str = "result.json"):
        with open(json_name, 'w', encoding="utf-8") as json_file:
            json.dump(self.data, json_file, indent=4, ensure_ascii=False)

    def write_to_csv(self, csv_name: str = "result.csv"):
        with open(csv_name, 'w', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, dialect="excel", delimiter="|")
            writer.writerow(['Name', 'Type', 'Size', 'Parent Directory'])
            for item in self.data:
                writer.writerow([
                    item['name'],
                    item['type'],
                    item['size'],
                    item['parent_directory']
                ])

    def write_to_pickle(self, pickle_name: str = "result.pickle"):
        with open(pickle_name, 'wb') as pickle_file:
            pickle.dump(self.data, pickle_file)


# 2
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

class ExtSorter():
    def __init__(self):
        self.__EXTENSIONS = {
            0: ["Audio", "mp3", "aac", "flac"],
            1: ["Video", "mp4", "avi", "mkv", "vbo"],
            2: ["Text", "txt", "ini"],
            3: ["Documents", "xlsx", "docx", "pdf"],
            # random unknown extension
            4: [''.join([string.ascii_lowercase[randint(0, 25)] if j != 0 else "Unknown"
                         for i in range(randint(1, 5 if j != 0 else 1))]) for j in range(10)]
        }

    def gen_file(self, count: int):
        for i in range(count):
            extension = randint(0, len(self.__EXTENSIONS.keys()) - 1)
            name = ''.join([string.ascii_lowercase[(randint(0, 25))] for _ in range(6)])
            with open(name + '.' + self.__EXTENSIONS.get(extension)[
                randint(1, len(self.__EXTENSIONS.get(extension)) - 1)], "w") as f:
                f.close()

    def sort_files(self):
        for file in os.listdir():
            if file == __file__.split('.')[-1]:
                continue
            extension = file.split(".")[-1]
            for i in range(len(self.__EXTENSIONS.keys()) - 1):
                group = self.__EXTENSIONS.get(i)
                if extension in group:
                    Path(group[0]).mkdir(exist_ok=True, parents=True)
                    shutil.move(file, group[0])

    def execute(self, count: int):
        self.gen_file(count)
        self.sort_files()


traverser = DirTraverser("C:\\Windows\\Branding")
print(traverser.show_path())
traverser.gen_list()
traverser.write_to_json()
traverser.write_to_csv()

sorter = ExtSorter()
sorter.execute(5)
