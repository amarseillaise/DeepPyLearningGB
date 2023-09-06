# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def func(text: str) -> list:
    return sorted([ord(x) for x in set(list(text))], reverse=True)


print(func("✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию."))