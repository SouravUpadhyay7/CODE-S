import numpy as np
import matplotlib.pyplot as plt

# Create a figure with a specified size
fig = plt.figure(figsize=(12, 6))

# Define x and y values
x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5, 5.1, 0.2)

# Create a meshgrid from x and y
X, Y = np.meshgrid(x, y)

# Calculate Z values based on the sine and cosine functions
Z = np.sin(X) * np.cos(Y)

# Add a subplot for the wireframe plot
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_wireframe(X, Y, Z)
ax.set_title('Wireframe plot')




# Show the plots
plt.show()
