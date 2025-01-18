# Shuffle elements of a list
import random
lst = list(map(int, input("Enter list elements: ").split()))
random.shuffle(lst)
print(f"Shuffled List: {lst}")
