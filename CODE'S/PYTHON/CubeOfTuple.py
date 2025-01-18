# 17. Cube of a Tuple
nums = tuple(map(int, input("Enter numbers separated by space: ").split()))
cubes = tuple(x**3 for x in nums)
print(f"Cubes: {cubes}")
