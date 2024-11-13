from datetime import datetime


def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        delta = date_today - target_date
        return delta.days
    except ValueError:
        return f"Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("неправильний формат"))