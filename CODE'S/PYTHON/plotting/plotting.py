import matplotlib.pyplot as plt

# Plot x vs y
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]
plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-10, 10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot of x vs y')
plt.show()
