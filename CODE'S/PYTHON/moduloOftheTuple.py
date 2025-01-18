# Taking input from the user for two tuples
tuple1 = tuple(map(int, input("Enter elements of the first tuple separated by space: ").split()))
tuple2 = tuple(map(int, input("Enter elements of the second tuple separated by space: ").split()))

# Finding the modulo of corresponding elements
# Only performs modulo if both tuples are of the same length
if len(tuple1) == len(tuple2):
    modulo_tuple = tuple(a % b for a, b in zip(tuple1, tuple2))
    print("Resulting tuple with modulo of elements:", modulo_tuple)
else:
    print("Error: Both tuples must have the same length.")
