# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def get_path_detail(f_path: str) -> tuple:
    *path, file = f_path.split("\\")
    *file_name, file_ext = file.split(".")
    return "\\".join(path) + "\\", ".".join(file_name), file_ext


# "C:\Windows\System32\cmd.exe"
f_path = r"C:\Windows\System32\ar-SA\mlang.dll.mui"
print(get_path_detail(f_path))
