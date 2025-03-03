# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    numbers_drawn = sample(number_pool, amount)
    numbers_drawn.sort()
    return numbers_drawn

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)