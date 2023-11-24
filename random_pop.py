# random_pop.py

import random


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    data = list(range(1, 45))
    while data: print(random_pop(data))
