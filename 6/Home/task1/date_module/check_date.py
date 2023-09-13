def is_valid_date(date: str) -> bool:
    day, month, year = date.split(".")
    days_from_month = {
        "01": 31,
        "02": 29 if _is_leap_year(int(year)) else 28,
        "03": 31,
        "05": 30,
        "06": 31,
        "07": 30,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }
    if not 0 < int(year) < 10000:
        return False

    if month not in days_from_month.keys():
        return False

    if days_from_month.get(month) < int(day):
        return False

    return True


def _is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
