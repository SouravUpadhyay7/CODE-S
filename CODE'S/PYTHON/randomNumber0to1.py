import random

random.seed(int(input("Enter a seed value for random number generation: ")))
random_float = random.random()

print(f"Generated random number between 0 and 1: {random_float}")
