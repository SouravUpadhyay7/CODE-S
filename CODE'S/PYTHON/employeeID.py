employee_id = input("enter employee ID :")
worked_hours = float(input("enter total worked hours in a month : "))
hourly_rate = float(input("enter amount received per hour"))

salary = worked_hours * hourly_rate
print("Employee ID : ", employee_id)

print("salary : $%.2f" %salary)