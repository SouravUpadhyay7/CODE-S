import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)
y = x  # Linear function f(x) = x

plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-10, 10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph of f(x) = x')
plt.show()
