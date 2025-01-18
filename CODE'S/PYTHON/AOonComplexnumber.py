# Operations on complex numbers
a = complex(input("Enter first complex number (e.g., 1+2j): "))
b = complex(input("Enter second complex number (e.g., 3+4j): "))
print(f"Addition: {a + b}, Subtraction: {a - b}, Multiplication: {a * b}, Division: {a / b}")

# Operations on fractions
from fractions import Fraction
frac1 = Fraction(input("Enter first fraction (e.g., 1/2): "))
frac2 = Fraction(input("Enter second fraction (e.g., 3/4): "))
print(f"Addition: {frac1 + frac2}, Subtraction: {frac1 - frac2}, Multiplication: {frac1 * frac2}, Division: {frac1 / frac2}")
