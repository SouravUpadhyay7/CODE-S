# Taking input from the user for the list of numbers, separated by space
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Creating a list of tuples with each number and its cube
result = [(num, num**3) for num in numbers]

# Printing the result
print("List of tuples (number, cube):", result)
