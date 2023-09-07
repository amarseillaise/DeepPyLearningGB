# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

account_sum = 0


def get_action() -> int:
    print("1 - пополнить счёт\n2 - снять деньги\nЛюбой другой символ - выйти\n")
    return int(input("Выберите действие: "))


def display_summ():
    print(f"Сумма вашего баланса: {account_sum}")


def is_odd_to_50(summ):
    return summ % 50 == 0


def cash_out():
    summ = int(input("Введите суму для снятия: "))
    if not is_odd_to_50(summ):
        print("Сумма должна быть кратна 50\n")
        return cash_out()
    if account_sum < summ:
        return "Нельзя снять больше, чем сумма на балансе\n"


while True:
    choose = get_action()
    if choose == 1:
        pass
    elif choose == 2:
        display_summ()
        print(cash_out())
        display_summ()
    else:
        exit(0)

