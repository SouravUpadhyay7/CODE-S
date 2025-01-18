# 14. Simple Interest Calculation
principal = float(input("Enter the amount: "))
rate = float(input("Enter the rate of interest: "))
years = float(input("Enter the number of years: "))
interest = (principal * rate * years) / 100
print(f"Simple Interest: {interest}")