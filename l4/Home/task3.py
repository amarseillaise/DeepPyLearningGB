# Возьмите задачу о банкомате из семинара l2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — l1.l5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - l3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в l5 млн, вычитать налог на богатство l10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

COMMISSION_PERCENT = 0.015
ADD_PERCENT = 0.03
TAX_FOR_REACH_LIMIT = 0.1
REACH_LIMIT = 5_000_000

account_sum = 0
operations_count = 0


def get_action() -> int:
    print("l1 - пополнить счёт\nl2 - снять деньги\nЛюбой другой символ - выйти\n")
    return int(input("Выберите действие: "))


def display_summ():
    global account_sum
    print(f"Сумма вашего баланса: {account_sum}")


def is_odd_to_50(summ):
    return summ % 50 == 0 and summ > 0


def calculate_tax(summ):
    tax = summ * COMMISSION_PERCENT
    if tax < 30:
        tax = 30
    elif tax > 600:
        tax = 600
    return tax


def add_percent(summ):
    percent = summ * ADD_PERCENT
    new_summ = summ + percent
    print(f"На ваш счёт зачислены проценты в размере {percent}, сумма вашего баланса составляет {new_summ}\n")
    return new_summ


def get_reach_tax():
    global account_sum
    tax_summ = account_sum * TAX_FOR_REACH_LIMIT
    account_sum -= tax_summ
    print(f"Вычтен налог на богатство в размере {tax_summ}, сумма вашего баланса составляет {account_sum}\n")



def cash_out():
    global account_sum
    summ = int(input("Введите суму для снятия: "))
    if not is_odd_to_50(summ):
        print("Сумма должна быть кратна 50 и больше 0\n")
        return cash_out()
    if account_sum < summ:
        return "Нельзя снять больше, чем сумма на балансе\n"

    tax = calculate_tax(summ)
    account_sum -= summ - tax
    return f"Заберите наличные в сумме {summ}. Комиссия составила {tax}\n"


def cash_in():
    global account_sum
    summ = int(input("Введите суму для пополнения: "))
    if not is_odd_to_50(summ):
        print("Сумма должна быть кратна 50 и больше 0\n")
        return cash_in()
    account_sum += summ
    return f"Внесены наличные в сумме {summ}\n"


if __name__ == "__main__":
    while True:
        choose = get_action()
        if account_sum > REACH_LIMIT:
            get_reach_tax()

        if choose == 1:
            display_summ()
            print(cash_in())
            display_summ()
        elif choose == 2:
            display_summ()
            print(cash_out())
            display_summ()
        else:
            exit(0)

        operations_count += 1
        if operations_count % 3 == 0:
            account_sum = add_percent(account_sum)
