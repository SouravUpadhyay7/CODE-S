from fractions import Fraction

num1 = int(input("Enter numerator for first fraction: "))
den1 = int(input("Enter denominator for first fraction: "))
num2 = int(input("Enter numerator for second fraction: "))
den2 = int(input("Enter denominator for second fraction: "))

frac1 = Fraction(num1, den1)
frac2 = Fraction(num2, den2)

sum_frac = frac1 + frac2
sub_frac = frac1 - frac2
mul_frac = frac1 * frac2
div_frac = frac1 / frac2

print(f"Sum: {sum_frac}")
print(f"Subtraction: {sub_frac}")
print(f"Multiplication: {mul_frac}")
print(f"Division: {div_frac}")
