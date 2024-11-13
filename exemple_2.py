# -*- coding: utf-8 -*-
from random import sample

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевіряємо коректність вхідних даних
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []

    # Генеруємо список унікальних чисел і сортуємо його
    lottery_numbers = sorted(sample(range(min_val, max_val + 1), quantity))
    return lottery_numbers

# Задаємо параметри
min_val = 1
max_val = 49
quantity = 6

# Викликаємо функцію
lottery_numbers = get_numbers_ticket(min_val, max_val, quantity)
print("Ваші лотерейні числа:", lottery_numbers)