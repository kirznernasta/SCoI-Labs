import random


def generate_list_of_even_numbers():
    return [element for element in random.sample(range(0, 1000), 15) if element % 2 == 0]
