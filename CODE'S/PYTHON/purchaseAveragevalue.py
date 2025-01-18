#python program that accepts two item weight and number of purchases ( float value ) ands calculate their average value


weight1 = float(input("Enter the weight of the first item: "))
weight2 = float(input("Enter the weight of the second item: "))


num_purchases1 = float(input("Enter the number of purchases for the first item: "))
num_purchases2 = float(input("Enter the number of purchases for the second item: "))


total_weight = (weight1 * num_purchases1) + (weight2 * num_purchases2)


total_purchases = num_purchases1 + num_purchases2


if total_purchases == 0:
    average_value = 0  
else:
    average_value = total_weight / total_purchases

print("The average value is:", average_value)

