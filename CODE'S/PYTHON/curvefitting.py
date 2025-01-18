# Curve fitting example
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linear(x, m, c):
    return m * x + c

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.2, 4.1, 6.0, 8.1, 10.2])
params, _ = curve_fit(linear, x_data, y_data)
plt.scatter(x_data, y_data, label="Data")
plt.plot(x_data, linear(x_data, *params), label="Fitted Curve", color="red")
plt.legend()
plt.show()
