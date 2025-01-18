#to calculate a bike average consumption from the given total distance (integer value) travlled (in km) and spent fuel 


total_distance = int(input("Enter the total distance traveled (in km): "))
fuel_spent = float(input("Enter the total fuel spent (in liters): "))


if fuel_spent == 0:
    print("Fuel spent cannot be zero.")
else:
    average_consumption = total_distance / fuel_spent
   
    print("The average fuel consumption is:", average_consumption, "km/liter")
