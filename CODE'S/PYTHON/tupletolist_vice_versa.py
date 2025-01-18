# Taking user input for list and tuple
my_list = list(map(int, input("Enter elements of the list separated by spaces: ").split()))
my_tuple = tuple(map(int, input("Enter elements of the tuple separated by spaces: ").split()))

# Adding tuple to list
my_list.extend(my_tuple)
print("List after adding tuple:", my_list)

# Adding list to tuple (create a new tuple)
new_tuple = my_tuple + tuple(my_list)
print("Tuple after adding list:", new_tuple)
