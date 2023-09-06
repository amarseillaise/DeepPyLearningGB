# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def func(**kwargs):
    result = {}
    # return {value: key for key, value in kwargs.items()}
    for key, value in kwargs.items():
        try:
            result.setdefault(value, key)
        except TypeError:
            result.setdefault(str(value), key)
    return result


dct = {"key": ["value0, value1"]}
lst = [0, 1, 2, 3]
dig = 11
txt = "word"
for key, value in func(arg0=dct, arg1=lst, arg2=dig, arg3=txt).items():
    print(f"{key} - {value}")
