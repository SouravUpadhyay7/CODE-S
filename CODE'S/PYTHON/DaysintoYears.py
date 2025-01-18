# 4. Days into Years, Weeks, and Days
days = int(input("Enter the number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print(f"{days} days is {years} years, {weeks} weeks, and {remaining_days} days.")