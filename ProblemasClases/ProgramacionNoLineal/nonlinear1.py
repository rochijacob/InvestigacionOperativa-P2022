import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def func(x):
  return (1/5)*x**6 - (5/4)*x**4 + 2*x**2

x = np.linspace(-2, 2, num=200)
plt.plot(x, func(x))

N  = 50
x0 = 0.0
candidato = np.inf

for ii in range(N):
  seed = x0 + 2*np.random.rand() - 2*np.random.rand()
  seed = 4*np.random.rand()-2  # Equivalentemente

  opt = optimize.minimize(fun=func, x0=seed)

  if opt.success is True and opt.fun < candidato:
    candidato = opt.fun
    punto_candidato = opt.x
    print(punto_candidato, candidato)

print('Final', punto_candidato, candidato)