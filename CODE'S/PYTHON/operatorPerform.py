# Taking two integers and an operator as input
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
opr = input("Enter an operator (+, -, *, /): ")

# Performing the operation
if opr == '+':
    result = n1 + n2
elif opr == '-':
    result = n1 - n2
elif opr == '*':
    result = n1 * n2
elif opr == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Undefined (division by zero)"
else:
    result = "Invalid operator"

print(f"Result: {result}")
