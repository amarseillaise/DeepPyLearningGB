# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def traverse_directory(directory):
    result = []

    for root, dirs, files in os.walk(directory):
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

    with open('result.json', 'w', encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)

    with open('result.csv', 'w', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, dialect="excel", delimiter="|")
        writer.writerow(['Name', 'Type', 'Size', 'Parent Directory'])
        for item in result:
            writer.writerow([
                item['name'],
                item['type'],
                item['size'],
                item['parent_directory']
            ])

    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)


traverse_directory("C:\\Users\\Marsel\\pythonProject\\DeepPyLearningGB")
