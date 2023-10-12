# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
#   [l3, l6] берутся буквы с l3 по l6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path


def mass_rename(*, postfix="", serial_num_count=1, src_ext="", dst_ext="", leave_range=[0,-1]):
    i = 0
    for file in os.listdir():
        *file_name, file_ext = file.split('.')
        if file_ext == src_ext:
            new_file_name = postfix
            new_file_name = new_file_name + "0" * (serial_num_count - len(str(i))) + str(i) if len(str(i)) < serial_num_count else new_file_name
            file_ext = dst_ext if dst_ext else file_ext
            new_file_name = str(file_name)[leave_range[0]:leave_range[1]] + new_file_name

            Path(file).rename(new_file_name + '.' + file_ext)
            i += 1


mass_rename(postfix="NEW", serial_num_count=3, src_ext="avi", dst_ext="NEWEXT", leave_range=[4, 7])
