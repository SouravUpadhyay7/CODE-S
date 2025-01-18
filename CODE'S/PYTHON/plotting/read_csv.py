# Read and display CSV
import csv
filename = input("Enter the CSV file name: ")
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Count lines in a CSV file
with open(filename, 'r') as file:
    count = sum(1 for line in file)
print(f"Number of lines: {count}")
