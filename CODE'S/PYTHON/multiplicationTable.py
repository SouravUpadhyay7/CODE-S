# Taking input for the number
num = int(input("Enter the number for multiplication table: "))

# Generating multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
