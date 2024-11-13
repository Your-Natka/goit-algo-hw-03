# -*- coding: utf-8 -*-
from datetime import datetime
start_date = "2020-10-09"

def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Use date_str instead of start_date
        print("Target date:", target_date)
        date_today = datetime.now().date()
        print("Today's date:", date_today)
        diff_day = (date_today - target_date)
        return diff_day.days
    except ValueError:
        return "Неправильний формат: {}".format(date_str)

# Call the function with the correct argument
print(get_days_from_today(start_date))
