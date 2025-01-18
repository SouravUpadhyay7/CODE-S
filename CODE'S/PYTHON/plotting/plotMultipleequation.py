import matplotlib.pyplot as plt  # Add this line

# Plot multiple equations
x = range(-10, 11)
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

plt.plot(x, y1, label='y=x')
plt.plot(x, y2, label='y=x^2')
plt.plot(x, y3, label='y=x^3')
plt.legend()
plt.show()
