# Randomly select items from a list
import random
lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter number of elements to select: "))
selected = random.sample(lst, k)
print(f"Randomly Selected Items: {selected}")
