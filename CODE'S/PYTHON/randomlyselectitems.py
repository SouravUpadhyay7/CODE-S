import random

n = int(input("Enter the number of random integers to generate: "))
lst = [random.randint(1, 100) for _ in range(n)]
num_to_select = int(input(f"Enter how many items to randomly select (max {n}): "))
selected_items = random.sample(lst, num_to_select)

print(f"List of random integers: {lst}")
print(f"Randomly selected items: {selected_items}")
