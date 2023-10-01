# 📌Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint


def find_number():
    a = randint(1, 100)
    b = randint(1, 10)

    def func():
        nonlocal a, b
        while b:
            print(f"Осталось попыток: {b}")
            guess = int(input("Введите число: "))
            if guess > a:
                print(f"Загаданное число меньше, чем {guess}")
            elif guess < a:
                print(f"Загаданное число больше, чем {guess}")
            else:
                print("В точку")
                break
            b -= 1
        else:
            print(f"У вас закончились попытки. Было загадано число {a}")

    return func


func = find_number()
func()
