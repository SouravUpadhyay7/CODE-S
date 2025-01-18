# Taking input from the user for the list elements, separated by space
user_list = input("Enter elements of the list separated by space: ").split()

# Taking input from the user for the tuple elements, separated by space
user_tuple = tuple(input("Enter elements of the tuple separated by space: ").split())

# Adding the tuple to the list
list_with_tuple = user_list + list(user_tuple)

# Adding the list to the tuple
tuple_with_list = tuple(user_list) + user_tuple

# Displaying the results
print("\nList after adding tuple:", list_with_tuple)
print("Tuple after adding list:", tuple_with_list)
