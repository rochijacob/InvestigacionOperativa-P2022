import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x, y):
   return 2*x**2 + y**2 + 0.1*(x+y)**2

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

plt.plot(x, f(x, y), color='red')

plt.show()