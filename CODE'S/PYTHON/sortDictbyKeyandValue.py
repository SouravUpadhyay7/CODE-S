# Taking user input for dictionary
input_dict = input("Enter dictionary elements in key:value format separated by commas (e.g., a:1,b:2): ")
my_dict = dict(item.split(":") for item in input_dict.split(","))

# Convert values to int
my_dict = {k: int(v) for k, v in my_dict.items()}

# Sort by key
sorted_by_key = dict(sorted(my_dict.items()))
print("Sorted by key:", sorted_by_key)

# Sort by value
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by value:", sorted_by_value)
