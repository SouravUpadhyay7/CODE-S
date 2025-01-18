import random

# Taking user input for range
min_value = int(input("Enter the minimum value for random number: "))
max_value = int(input("Enter the maximum value for random number: "))

# Ensure min_value is less than or equal to max_value
if min_value > max_value:
    min_value, max_value = max_value, min_value

# Random value between two integers (inclusive)
rand_value = random.randint(min_value, max_value)
print("Random value:", rand_value)

