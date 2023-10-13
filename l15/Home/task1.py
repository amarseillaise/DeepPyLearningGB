# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import sys
import os
import logging
from collections import namedtuple
import argparse

Entry = namedtuple('Entry', ['name', 'extension', 'is_directory', 'parent_directory'])


def gather_directory_info(directory_path):
    try:
        logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s %(message)s', encoding="UTF-8")
        logger = logging.getLogger()

        entries = []

        if not os.path.exists(directory_path):
            logger.error(f"Directory '{directory_path}' does not exist.")
            return entries

        for entry in os.listdir(directory_path):
            entry_path = os.path.join(directory_path, entry)

            if os.path.isfile(entry_path):
                name = os.path.splitext(entry)[0]
                extension = os.path.splitext(entry)[1]
                is_directory = False
            elif os.path.isdir(entry_path):
                name = entry
                extension = ""
                is_directory = True
            else:
                continue

            parent_directory = os.path.basename(directory_path)

            entry_obj = Entry(name=name, extension=extension, is_directory=is_directory,
                              parent_directory=parent_directory)
            entries.append(entry_obj)

            logger.info(
                f"Name: {entry_obj.name}, Extension: {entry_obj.extension}, Is Directory: {entry_obj.is_directory}, Parent Directory: {entry_obj.parent_directory}")

        return entries

    except Exception as e:
        logger.exception("An exception occurred")


parser = argparse.ArgumentParser()
parser.add_argument("-p", dest="path", type=str, required=True)
directory_path = parser.parse_args().path
directory_info = gather_directory_info(directory_path)
