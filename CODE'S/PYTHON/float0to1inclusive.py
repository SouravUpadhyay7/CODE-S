import random

random_float_1 = random.random()  # Between 0 and 1
low = float(input("Enter the lower bound for the range: "))
high = float(input("Enter the upper bound for the range: "))
random_float_2 = random.uniform(low, high)  # Between low and high

print(f"Random float between 0 and 1: {random_float_1}")
print(f"Random float between {low} and {high}: {random_float_2}")
