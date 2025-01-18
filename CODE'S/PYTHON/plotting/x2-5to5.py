import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)  # Creates an array of 100 points from -5 to 5
y = x ** 2

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph of f(x) = x^2')
plt.show()
