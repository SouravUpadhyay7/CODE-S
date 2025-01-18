# Taking input from the user for two tuples
tuple1 = tuple(input("Enter elements of the first tuple separated by space: ").split())
tuple2 = tuple(input("Enter elements of the second tuple separated by space: ").split())

# Displaying original tuples
print("\nOriginal tuples:")
print("First tuple:", tuple1)
print("Second tuple:", tuple2)

# Swapping the tuples
tuple1, tuple2 = tuple2, tuple1

# Displaying swapped tuples
print("\nAfter swapping:")
print("First tuple:", tuple1)
print("Second tuple:", tuple2)
