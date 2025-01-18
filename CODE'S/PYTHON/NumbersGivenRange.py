def is_within_range(number, start, end):
    return start <= number <= end

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if is_within_range(number, start, end):
    print(f"{number} is within the range {start} to {end}")
else:
    print(f"{number} is outside the range {start} to {end}")
