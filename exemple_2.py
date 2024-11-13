import random

def get_numbers_ticket(min_val, max_val, quantity):
    if min_val <= 1 or max_val >= 49 or quantity <= 6 or quantity > (max_val - min_val + 1):
        return []
    else:
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

