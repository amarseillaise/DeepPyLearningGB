# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def func(digits: str) -> dict:
    result = {}
    for i in range(int(digits.split()[0]), int(digits.split()[1]) + 1):
        result.setdefault(chr(i), i)
    return result


for key, value in func("1000 1071").items():
    print(f"{key} - {value}")
