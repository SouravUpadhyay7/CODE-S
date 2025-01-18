# Taking input from the user for the original tuple
original_tuple = tuple(input("Enter elements of the tuple separated by space: ").split())

# Taking indices to copy as user input, separated by space, and converting to integers
indices_to_copy = list(map(int, input("Enter indices of elements to copy separated by space: ").split()))

# Creating a new tuple with specific elements
new_tuple = tuple(original_tuple[i] for i in indices_to_copy)

# Printing the new tuple
print("New tuple:", new_tuple)

