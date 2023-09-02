from fractions import Fraction
import math


def task2():
    # 2.Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
    # Функцию hex используйте для проверки своего результата

    BASE = 16
    HEX_DIGIT_CHANGER = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }

    result = ''
    digit = int(input("целое десятичное число: "))
    primary_digit = digit

    while digit > 0:
        temp = digit % BASE if digit % BASE < 10 else HEX_DIGIT_CHANGER.get(digit % BASE)
        result = str(temp) + str(result)
        digit //= BASE
    result += f"\nПроверка функцией hex(): {hex(primary_digit).upper()[2::]}"

    return result


def task3():
    # 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
    # Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

    first_fraction = tuple(input('Введите первую дробь в формате "a/b": ').split("/"))
    second_fraction = tuple(input('Введите вторую дробь в формате "a/b": ').split("/"))

    first_fraction_simple = Fraction(int(first_fraction[0]), int(first_fraction[1]))
    second_fraction_simple = Fraction(int(second_fraction[0]), int(second_fraction[1]))

    denumerator = math.lcm(int(first_fraction[1]), int(second_fraction[1]))  # Общий знаменатель через НОК
    numerator_sum = int((int(first_fraction[0]) * (denumerator // int(first_fraction[1]))
                         + int(second_fraction[0]) * (denumerator // int(second_fraction[1]))))

    summ = [numerator_sum, denumerator]
    simple_summ = first_fraction_simple + second_fraction_simple

    product = [int(first_fraction[0]) * int(second_fraction[0]), int(first_fraction[1]) * int(second_fraction[1])]
    simple_product = first_fraction_simple * second_fraction_simple

    #  Сокращаем дроби
    for fraction in summ, product:
        gcd = math.gcd(fraction[0], fraction[1])
        while gcd not in (1, 0):
            fraction[0] //= gcd
            fraction[1] //= gcd
            gcd = math.gcd(fraction[0], fraction[1])

    summ = f"{summ[0]}/{summ[1]}"
    product = f"{product[0]}/{product[1]}"
    result = (f"Сумма: {summ}\n"
              f"Произведение: {product}\n"
              f"Сумма через Fraction(): {simple_summ}\n"
              f"Произведение через Fraction(): {simple_product}")

    return result


if __name__ == "__main__":
    print(task2())
    print(task3())
