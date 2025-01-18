# 10. Sum of Two Integers with Overflow Check
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
total = a + b
if a >= 0 and b >= 0 and total <= 80:
    print(f"Sum: {total}")
else:
    print("Overflow")