# -*- coding: utf-8 -*-
from datetime import datetime


def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        delta_days = date_today - target_date
        return delta_days.days
    except ValueError:
        return "Неправильний формат: {}".format(date_str)

print(get_days_from_today("неправильний формат"))
print(get_days_from_today("2020-10-09"))
