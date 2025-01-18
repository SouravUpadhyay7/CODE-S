def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Even numbers:")
print_even_numbers(numbers)
