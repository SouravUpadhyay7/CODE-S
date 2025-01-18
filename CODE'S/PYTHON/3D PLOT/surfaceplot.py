import numpy as np
import matplotlib.pyplot as plt

# Create a figure with specified size
fig = plt.figure(figsize=(12, 10))

# Add 3D axes
ax = plt.axes(projection='3d')

# Generate x and y values from -5 to 5 with a step of 0.2
x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5, 5.1, 0.2)

# Create a meshgrid from x and y
X, Y = np.meshgrid(x, y)

# Calculate Z values based on the sine and cosine functions
Z = np.sin(X) * np.cos(Y)

# Create the surface plot with the cividis colormap
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.cividis)

# Set labels for each axis with padding
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

# Add color bar for the surface plot
fig.colorbar(surf, shrink=0.5, aspect=8)

# Show the plot
plt.show()
