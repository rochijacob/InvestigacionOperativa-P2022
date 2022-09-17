#No Lineal
from scipy import optimize
import numpy as np

def f_obj(x):
    return (x[0]-1)**2 + (x[1]-2)**2


N = 1000
x_opt = []
f_opt = np.inf

for i in range(N):
    x0 = np.random.rand(2)
    opt = optimize.minimize(f_obj, x0)
    if opt.fun < f_opt:
        x_opt = opt.x
        f_opt = opt.fun

print('Funcion optimizacion devuelve: ', opt)