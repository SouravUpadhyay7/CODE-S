import numpy as np
import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure(figsize=(8, 8))

# Add 3D axes
ax = plt.axes(projection='3d')

# Enable grid
ax.grid()

# Define the parameter t
t = np.arange(0, 10 * np.pi, np.pi / 50)

# Parametric equations for x and y
x = np.sin(t)
y = np.cos(t)

# Plotting the 3D curve
ax.plot3D(x, y, t)

# Set title for the plot
ax.set_title('3D Parametric Plot')

# Set labels for each axis
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('t', labelpad=20)

# Show the plot
plt.show()
