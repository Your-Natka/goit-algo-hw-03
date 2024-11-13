# -*- coding: utf-8 -*-  # Додаємо кодування для коректного відображення тексту

import re

def normalize_phone(phone):
    clean_number = re.sub(r'\D', '', phone)  # Видаляємо всі нецифрові символи
    if not clean_number.startswith('38') and not clean_number.startswith('0'):
        clean_number = '38' + clean_number  # Додаємо код країни
    elif clean_number.startswith('0'):
        clean_number = '380' + clean_number[1:]  # Замінюємо '0' на '380'
    return "+" + clean_number

# Приклад використання
raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормалізуємо номери
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Виводимо результати
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
