import numpy as np
import matplotlib.pyplot as plt

# Generate random data for x, y, and z
x = np.random.random(50)
y = np.random.random(50)
z = np.random.random(50)

# Create a figure
fig = plt.figure(figsize=(10, 10))

# Add 3D axes
ax = plt.axes(projection='3d')

# Enable grid
ax.grid()

# Scatter plot with red points and size of 50
ax.scatter(x, y, z, c='r', s=50)

# Set title for the plot
ax.set_title('3D Scatter Plot')

# Set labels for each axis
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

# Show the plot
plt.show()
