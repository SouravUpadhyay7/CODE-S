import numpy as np

# Define the x and y arrays
x = [1, 2, 3, 4]
y = [3, 4, 5]

# Generate meshgrid
X, Y = np.meshgrid(x, y)

# Print the X and Y meshgrid results
print("X:")
print(X)
print("\nY:")
print(Y)
