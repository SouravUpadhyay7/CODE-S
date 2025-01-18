import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
random_value = random.randint(low, high)
random_multiple_of_7 = random.choice([x for x in range(0, 71, 7)])

print(f"Random value between {low} and {high}: {random_value}")
print(f"Random multiple of 7 between 0 and 70: {random_multiple_of_7}")
