# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# 📌Преобразуйте его в дату в текущем году.
# 📌Логируйте ошибки, если текст не соответсвует формату.

import re
import logging
import datetime

DAYS_OF_WEEK = (
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
)

MONTHS = (
    "январь",
    "февраль",
    "март",
    "апрель",
    "май",
    "июнь",
    "июль",
    "август",
    "сентябрь",
    "октябрь",
    "ноябрь",
    "декабрь",

)

FORMAT = "{asctime} | {levelname} -> {msg}"

logging.basicConfig(filename="log.log", encoding="UTF-8", level="ERROR", filemode='a', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def parse_date(parsed_str: str, patterns):
    for pattern in patterns:
        match = re.match(pattern[:-1], parsed_str.lower())
        if match:
            return pattern
    logger.error(f"Неправильный формат даты в {parsed_str}")


def date_converter(date_word: str):
    number, weekday, month = date_word.split()

    number = int(re.match(r"\d", number).group())
    weekday = DAYS_OF_WEEK.index(parse_date(weekday, DAYS_OF_WEEK))
    month = MONTHS.index(parse_date(month, MONTHS)) + 1
    year = datetime.datetime.now().year

    temp_number = number
    for i in range(1, 33):
        try:
            week = datetime.date(year, month, i).weekday()
        except ValueError:
            logger.error(f"{number} {DAYS_OF_WEEK[weekday]} нет в месяце {MONTHS[month - 1]}")
            return
        if week == weekday:
            temp_number -= 1
            if not temp_number:
                break

    return datetime.date(year, month, i)


print(date_converter("3й понедельник апреля"))
