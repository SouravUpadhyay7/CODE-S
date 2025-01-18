import random

seed_value = int(input("Enter a seed value for random number generation: "))
random.seed(seed_value)
random_float = random.random()

print(f"Generated float between 0 and 1: {random_float}")
